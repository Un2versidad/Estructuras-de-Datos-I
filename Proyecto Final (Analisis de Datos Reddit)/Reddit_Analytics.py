import asyncio
import asyncpraw
import asyncprawcore
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os
import logging
import json
from pathlib import Path
from dotenv import load_dotenv
import shutil
import glob

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CONFIG = {
    "post_limit": 10,
    "community_limit": 3,
    "cache_dir": ".cache"
}

async def verify_reddit_auth(reddit):
    try:
        user = await reddit.user.me()
        logger.info(f"Reddit instance authenticated: {user.name}")
        return True
    except asyncprawcore.exceptions.RequestException as e:
        logger.error(f"Authentication failed: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during authentication: {e}")
        return False

def load_cache(search_tag):
    cache_file = Path(CONFIG["cache_dir"]) / f"{search_tag.replace(' ', '_')}.json"
    if cache_file.exists():
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_cache(search_tag: str, data: dict) -> None:
    cache_file = Path(CONFIG["cache_dir"]) / f"{search_tag.replace(' ', '_')}.json"
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    with open(cache_file, 'w', encoding='utf-8') as f:
        f.write(json_str)

async def get_user_info(reddit, user):
    try:
        if not user or not hasattr(user, 'name') or user.name is None:
            return {"name": "Unknown", "post_karma": 0, "comment_karma": 0}
        redditor = await reddit.redditor(user.name)
        await redditor.load()
        try:
            post_karma = getattr(redditor, 'link_karma', 0)
            comment_karma = getattr(redditor, 'comment_karma', 0)
        except AttributeError:
            post_karma = 0
            comment_karma = 0
            logger.warning(f"Karma attributes not available for {redditor.name}")
        return {
            "name": redditor.name,
            "post_karma": post_karma,
            "comment_karma": comment_karma
        }
    except Exception as e:
        logger.warning(f"User info not available: {e}")
        return {"name": "Unknown", "post_karma": 0, "comment_karma": 0}

async def get_latest_event(reddit, subreddit_name, search_tag):
    try:
        subreddit = await reddit.subreddit(subreddit_name)
        async for submission in subreddit.search(search_tag, limit=CONFIG["post_limit"], sort="new"):
            author_info = await get_user_info(reddit, submission.author)
            logger.info(f"Fetched submission: {submission.title} with {submission.score} upvotes")

            media = []

            # 1. Verificar si es un video
            if hasattr(submission, 'media') and submission.media and 'reddit_video' in submission.media:
                video_url = submission.media['reddit_video'].get('fallback_url')
                if video_url:
                    media.append({"type": "video", "url": video_url})
                    logger.info(f"Found video URL: {video_url}")
            elif submission.url and submission.url.endswith('.mp4'):
                media.append({"type": "video", "url": submission.url})
                logger.info(f"Found video URL in submission URL: {submission.url}")

            # 2. Verificar si es una imagen simple
            if hasattr(submission, 'url') and submission.url:
                if submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    media.append({"type": "image", "url": submission.url})
                    logger.info(f"Found image URL: {submission.url}")

            # 3. Verificar si hay una imagen en el preview
            if hasattr(submission, 'preview') and submission.preview:
                images = submission.preview.get('images', [])
                if images:
                    image_url = images[0]['source'].get('url')
                    if image_url and image_url not in [m["url"] for m in media]:
                        media.append({"type": "image", "url": image_url})
                        logger.info(f"Found image URL in preview: {image_url}")

            # 4. Verificar si es una galería
            if hasattr(submission, 'is_gallery') and submission.is_gallery:
                if hasattr(submission, 'gallery_data') and submission.gallery_data:
                    for item in submission.gallery_data.get('items', []):
                        media_id = item.get('media_id')
                        if media_id:
                            metadata = submission.media_metadata.get(media_id, {})
                            if metadata.get('e') == 'Image':
                                image_url = metadata.get('s', {}).get('u')
                                if image_url and image_url not in [m["url"] for m in media]:
                                    media.append({"type": "image", "url": image_url})
                                    logger.info(f"Found gallery image URL: {image_url}")
                else:
                    logger.warning(f"Gallery detected but no gallery_data available for {submission.id}")

            # Obtener métricas de engagement
            awards = submission.total_awards_received if hasattr(submission, 'total_awards_received') else 0
            total_comments = submission.num_comments if hasattr(submission, 'num_comments') else 0

            return {
                "title": submission.title,
                "author": author_info,
                "created_at": datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                "body": submission.selftext if submission.selftext else "No texto disponible",
                "score": submission.score,
                "url": f"https://www.reddit.com{submission.permalink}",
                "media": media,
                "subreddit": submission.subreddit.display_name,
                "id": submission.id,
                "engagement": {
                    "upvotes": submission.score,
                    "total_comments": total_comments,
                    "awards": awards,
                    "share_url": f"https://www.reddit.com{submission.permalink}"  # URL para compartir
                }
            }
        logger.warning(f"No submissions found for {search_tag} in {subreddit_name}")
        return None
    except Exception as e:
        logger.error(f"Error fetching latest event: {e}")
        return None

async def get_comments(reddit, submission_id, comment_limit=20):
    try:
        if not submission_id:
            logger.warning("No submission ID provided for comments")
            return {"total_comments": 0, "comments": []}

        submission = await reddit.submission(id=submission_id)
        await submission.load()
        logger.info(f"Fetched submission: {submission.title} with {submission.score} upvotes")

        # Obtener el conteo total de comentarios
        total_comments = submission.num_comments
        logger.info(f"Total comments in submission: {total_comments}")

        # Expandir todos los comentarios disponibles
        await submission.comments.replace_more(limit=None)  # Expandir todos los "MoreComments"
        comment_list = submission.comments.list()

        # Filtrar comentarios válidos (ignorar comentarios eliminados o sin cuerpo)
        valid_comments = [
            comment for comment in comment_list
            if hasattr(comment, 'body') and comment.body and comment.body != "[deleted]" and comment.body != "[removed]"
        ]

        # Log para depurar cuántos comentarios válidos se encontraron
        logger.info(f"Found {len(valid_comments)} valid comments out of {total_comments}")

        # Si hay menos de 20 comentarios, mostramos todos; si no, aplicamos el límite
        effective_limit = len(valid_comments) if len(valid_comments) <= 20 else comment_limit
        limited_comments = valid_comments[:effective_limit]
        logger.info(f"Showing {len(limited_comments)} comments out of {total_comments} (valid: {len(valid_comments)})")

        # Procesar los comentarios válidos
        comments = []
        for comment in limited_comments:
            if hasattr(comment, 'author') and comment.author:
                try:
                    author_info = await get_user_info(reddit, comment.author)
                    comments.append({
                        "user": author_info,
                        "body": comment.body,
                        "score": comment.score
                    })
                except Exception as e:
                    logger.warning(f"Error processing comment by {comment.author}: {e}")
                    continue
            else:
                logger.warning(f"Skipping comment with missing or invalid author: {comment.id}")

        return {
            "total_comments": total_comments,
            "comments": comments
        }
    except Exception as e:
        logger.error(f"Error fetching comments: {e}")
        return {"total_comments": 0, "comments": []}

async def get_communities(reddit, search_tag, limit=CONFIG["community_limit"]):
    communities = []
    try:
        async for subreddit in reddit.subreddits.search(search_tag, limit=limit):
            moderators = await subreddit.moderator()
            active_users = []
            for moderator in moderators[:3]:
                user_info = await get_user_info(reddit, moderator)
                active_users.append(user_info)
            communities.append({
                "name": subreddit.display_name,
                "size": subreddit.subscribers,
                "description": subreddit.public_description or "No description available",
                "active_users": active_users
            })
        return communities
    except Exception as e:
        logger.error(f"Error fetching communities: {e}")
        return []

def delete_previous_reports():
    report_files = glob.glob("report_*.html")
    for file in report_files:
        try:
            os.remove(file)
            logger.info(f"Deleted previous report: {file}")
        except Exception as e:
            logger.error(f"Error deleting previous report {file}: {e}")


async def generate_report(reddit, search_tag):
    cache_key = search_tag.lower().replace(" ", "_")
    logger.info(f"Fetching fresh data for {search_tag}")
    subreddit = None
    async for sub in reddit.subreddits.search(search_tag, limit=1):
        subreddit = sub
        break
    if not subreddit:
        subreddit = await reddit.subreddit("all")
    latest_event = await get_latest_event(reddit, subreddit.display_name, search_tag)

    if not latest_event:
        latest_event = {
            "title": "No data available",
            "author": {"name": "Unknown"},
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "body": "No texto disponible",
            "score": 0,
            "url": "",
            "media": [],
            "subreddit": subreddit.display_name if subreddit else "all",
            "id": None,
            "engagement": {
                "upvotes": 0,
                "total_comments": 0,
                "awards": 0,
                "share_url": ""
            }
        }

    # Obtener todos los comentarios disponibles
    comments_data = await get_comments(reddit, latest_event["id"])
    comments = comments_data["comments"]
    logger.info(f"Passing {len(comments)} comments to the HTML")

    communities = await get_communities(reddit, search_tag)

    report_data = {
        search_tag.lower(): {
            "tag": search_tag,
            "event": latest_event,
            "engagement": latest_event["engagement"],
            "comments": comments,
            "communities": communities
        }
    }
    save_cache(cache_key, {"timestamp": datetime.now().isoformat(), "data": report_data})
    logger.info(f"Generated report data: {report_data}")

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report.html')
    report_filename = f'report_{search_tag.lower().replace(" ", "_")}_{int(datetime.now().timestamp())}.html'
    try:
        html_content = template.render(data=report_data[search_tag.lower()])
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        logger.info(f"Report generated: {report_filename}")
        return report_filename
    except Exception as e:
        logger.error(f"Error rendering template for {search_tag}: {e}")
        return None

async def main():
    reddit = asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )
    if not await verify_reddit_auth(reddit):
        logger.error("Authentication failed. Exiting.")
        return

    # Eliminar reportes previos al inicio del programa
    delete_previous_reports()

    cache_dir = Path(CONFIG["cache_dir"])
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
        logger.info("Cleared cache directory")

    try:
        while True:
            print("\nIntroduce un tema para buscar (o 'salir' para terminar):")
            search_tag = input().strip().capitalize()
            if search_tag.lower() == 'salir':
                break
            if not search_tag:
                print("Por favor, ingresa un tema válido.")
                continue

            logger.info(f"Procesando búsqueda para el tema: {search_tag}")
            try:
                report_filename = await generate_report(reddit, search_tag)
                if report_filename:
                    print(f"Reporte generado: {report_filename}")
            except Exception as e:
                logger.error(f"Error generating report for {search_tag}: {e}")
    finally:
        await reddit.close()
        logger.info("Reddit session closed successfully")

if __name__ == "__main__":
    asyncio.run(main())