import asyncio
import asyncpraw
import requests
from datetime import datetime, timezone
from jinja2 import Template
from pathlib import Path
from dotenv import load_dotenv
import os
import logging
import shutil
import glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import colorama
import sys
import webbrowser
import random
from colorama import Fore, Style
from typing import Dict, Any, Optional

# Inicializar colorama
colorama.init()

# Configuración de logging (solo archivo)
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("reddit_analyser.log")]
)
logger = logging.getLogger(__name__)

# Configuración global
CONFIG = {
    "post_limit": 10,
    "community_limit": 3,
    "cache_dir": ".cache",
    "download_template": False,
    "comment_limit_display": 20,
    "comment_limit_timeline": 50,
    "community_post_limit": 5
}

# URL de plantillas en GitHub
REPORT_TEMPLATE_URL = "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Proyecto%20Final%20(Analisis%20de%20Datos%20Reddit)/report.html"
USER_REPORT_TEMPLATE_URL = "https://raw.githubusercontent.com/Un2versidad/Estructuras-de-Datos-I/refs/heads/main/Proyecto%20Final%20(Analisis%20de%20Datos%20Reddit)/user_report_template.html"

# Funciones de Interfaz de Usuario
def print_banner() -> None:
    print(f"{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}║       Reddit Analyser v1.0         ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}╚════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Powered by Reddit - {datetime.now().strftime('%Y-%m-%d')}{Style.RESET_ALL}\n")

def print_menu() -> None:
    print(f"{Fore.YELLOW}{Style.BRIGHT}=== Opciones del Menú ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}  1. Analizar un usuario de Reddit{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  2. Buscar un tema{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  3. Salir{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}======================={Style.RESET_ALL}")

def print_success(message: str) -> None:
    print(f"{Fore.GREEN}{Style.BRIGHT}✓ {message}{Style.RESET_ALL}")

def print_error(message: str) -> None:
    print(f"{Fore.RED}{Style.BRIGHT}✗ {message}{Style.RESET_ALL}")

def print_info(message: str) -> None:
    print(f"{Fore.CYAN}{Style.BRIGHT}ℹ {message}{Style.RESET_ALL}")

def progress_bar(duration: float = 2, width: int = 30) -> None:
    steps = 20
    sleep_time = duration / steps
    for i in range(steps + 1):
        progress = i / steps
        bar = '█' * int(width * progress) + '-' * (width - int(width * progress))
        sys.stdout.write(f"\r{Fore.YELLOW}Procesando: [{bar}] {int(progress * 100)}%")
        sys.stdout.flush()
        time.sleep(sleep_time)
    sys.stdout.write("\r" + " " * (width + 15) + "\r")
    sys.stdout.flush()

async def search_animation(task: asyncio.Task) -> None:
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while not task.done():
        sys.stdout.write(f"\r{Fore.CYAN}Buscando {animation[i % len(animation)]}{Style.RESET_ALL}")
        sys.stdout.flush()
        i += 1
        await asyncio.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

# Verificación de Plantillas
def verify_template(template_path: Path, template_url: str) -> Optional[str]:
    if not CONFIG["download_template"] and template_path.exists():
        logger.info(f"Usando plantilla local {template_path}")
        print_info(f"Usando plantilla local {template_path.name}")
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()

    try:
        response = requests.get(template_url, timeout=10)
        response.raise_for_status()
        github_content = response.text
        logger.info(f"Descargando plantilla {template_path} desde GitHub.")
        print_info(f"Descargando plantilla {template_path.name} desde GitHub.")
        template_path.parent.mkdir(parents=True, exist_ok=True)
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(github_content)
        return github_content
    except requests.RequestException as e:
        logger.error(f"No se pudo descargar la plantilla desde GitHub: {e}")
        if template_path.exists():
            logger.warning(f"Usando plantilla local existente {template_path} como fallback.")
            print_info(f"Usando plantilla local {template_path.name} como fallback.")
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        print_error(f"No se pudo descargar la plantilla y no existe localmente: {e}")
        return None

# Autenticación de Reddit
async def verify_reddit_auth(reddit: asyncpraw.Reddit) -> bool:
    try:
        user = await reddit.user.me()
        if user:
            logger.info(f"Autenticado como: {user.name}")
            return True
        logger.warning("Autenticación verificada, pero no se obtuvo información del usuario.")
        return True
    except Exception as e:
        logger.error(f"Fallo en la autenticación: {e}")
        return False

# Función de Utilidad Time Ago
def calculate_time_ago(timestamp_utc):
    if not timestamp_utc:
        return "N/A"
    try:
        now_utc = datetime.now(timezone.utc)
        if isinstance(timestamp_utc, (int, float)):
            dt_utc = datetime.fromtimestamp(timestamp_utc, timezone.utc)
        elif isinstance(timestamp_utc, datetime) and timestamp_utc.tzinfo is None:
            dt_utc = timestamp_utc.replace(tzinfo=timezone.utc)
        elif isinstance(timestamp_utc, datetime):
            dt_utc = timestamp_utc.astimezone(timezone.utc)
        else:
            return "Fecha inválida"

        diff = now_utc - dt_utc
        seconds = max(0, int(diff.total_seconds()))

        if seconds < 60:
            return f"hace {seconds} seg"
        minutes = seconds / 60
        if minutes < 60:
            return f"hace {int(minutes)} min"
        hours = minutes / 60
        if hours < 24:
            return f"hace {int(hours)} h"
        days = hours / 24
        if days < 7:
            return f"hace {int(days)} d"
        weeks = days / 7
        if weeks < 4.345:
            return f"hace {int(weeks)} sem"
        months = days / 30.417
        if months < 12:
            return f"hace {int(months)} mes"
        years = days / 365.2425
        return f"hace {int(years)} a"
    except Exception as e:
        logger.error(f"Error calculating time ago for {timestamp_utc}: {e}")
        return "Fecha desconocida"

# Obtener información de usuario
async def get_user_info(reddit: asyncpraw.Reddit, user: Any) -> Dict[str, Any]:
    try:
        if not user or not hasattr(user, 'name') or user.name is None:
            return {"name": "Desconocido", "post_karma": 0, "comment_karma": 0, "total_karma": 0}
        redditor = await reddit.redditor(user.name)
        await redditor.load()
        post_karma = getattr(redditor, 'link_karma', 0)
        comment_karma = getattr(redditor, 'comment_karma', 0)
        return {
            "name": redditor.name,
            "post_karma": post_karma,
            "comment_karma": comment_karma,
            "total_karma": post_karma + comment_karma
        }
    except Exception as e:
        logger.warning(f"Información del usuario '{getattr(user, 'name', 'N/A')}' no disponible: {e}")
        return {"name": "Desconocido", "post_karma": 0, "comment_karma": 0, "total_karma": 0}

# Obtener evento más reciente
async def get_latest_event(reddit: asyncpraw.Reddit, subreddit_name: str, search_tag: str) -> Optional[Dict[str, Any]]:
    try:
        subreddit = await reddit.subreddit(subreddit_name)
        async for submission in subreddit.search(search_tag, limit=CONFIG["post_limit"], sort="new"):
            author_info = await get_user_info(reddit, submission.author)
            media = []
            if submission.media and 'reddit_video' in submission.media:
                media.append({"type": "video", "url": submission.media['reddit_video'].get('fallback_url', '')})
            elif submission.url.endswith('.mp4'):
                media.append({"type": "video", "url": submission.url})
            if submission.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                media.append({"type": "image", "url": submission.url})
            return {
                "title": submission.title,
                "author": author_info,
                "created_at": datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                "body": submission.selftext or "Sin texto disponible",
                "score": submission.score,
                "url": f"https://www.reddit.com{submission.permalink}",
                "media": media,
                "subreddit": submission.subreddit.display_name,
                "id": submission.id,
                "engagement": {
                    "upvotes": submission.score,
                    "total_comments": submission.num_comments,
                    "awards": getattr(submission, 'total_awards_received', 0),
                    "share_url": f"https://www.reddit.com{submission.permalink}"
                }
            }
        return None
    except Exception as e:
        logger.error(f"Error al obtener el último evento: {e}")
        return None

# Obtener comentarios
async def get_comments(reddit: asyncpraw.Reddit, submission_id: str, comment_limit: int) -> Dict[str, Any]:
    if not submission_id:
        return {"total_comments": 0, "comments": []}
    try:
        submission = await reddit.submission(id=submission_id)
        await submission.load()
        await submission.comments.replace_more(limit=0)
        comments_list = []
        for comment in submission.comments.list()[:comment_limit]:
            if hasattr(comment, 'body') and hasattr(comment, 'author') and hasattr(comment, 'created_utc') and hasattr(
                    comment, 'score') and comment.body not in ("[deleted]", "[removed]"):
                user_info = await get_user_info(reddit, comment.author)
                created_utc_timestamp = comment.created_utc
                comment_data = {
                    "type": "comment",
                    "id": comment.id,
                    "user": user_info,
                    "body": comment.body,
                    "score": comment.score,
                    "created_utc": created_utc_timestamp,
                    "created_at": datetime.fromtimestamp(created_utc_timestamp).strftime('%Y-%m-%d %H:%M:%S'),
                    "time_ago": calculate_time_ago(created_utc_timestamp),
                    "url": f"https://www.reddit.com{comment.permalink}"
                }
                comments_list.append(comment_data)

        total_comments_count = submission.num_comments
        logger.info(
            f"Obtenidos {len(comments_list)} comentarios de {total_comments_count} totales para {submission_id}")
        return {"total_comments": total_comments_count, "comments": comments_list}

    # noinspection PyUnresolvedReferences
    except asyncpraw.exceptions.RedditAPIException as e:
        if "404" in str(e) or "NOT_FOUND" in str(e).upper():
            logger.error(f"Error: Submission con ID '{submission_id}' no encontrado.")
            return {"total_comments": 0, "comments": []}
        logger.error(f"Error al obtener comentarios para {submission_id}: {str(e)}")
        return {"total_comments": 0, "comments": []}
    except Exception as e:
        logger.error(f"Error inesperado al obtener comentarios para {submission_id}: {e}")
        return {"total_comments": 0, "comments": []}

# Obtener comunidades
async def get_communities(reddit: asyncpraw.Reddit, search_tag: str, limit: int = CONFIG["community_limit"]) -> list:
    try:
        communities = []
        logger.info(f"Buscando hasta {limit} comunidades para '{search_tag}'...")
        async for subreddit in reddit.subreddits.search(search_tag, limit=limit):
            try:
                moderators_list = await subreddit.moderator()
                active_users_sample = [await get_user_info(reddit, mod) for mod in moderators_list[:3]]
            # noinspection PyUnresolvedReferences
            except asyncpraw.exceptions.RedditAPIException as e:
                if "403" in str(e) or "FORBIDDEN" in str(e).upper():
                    logger.warning(
                        f"No se pudo obtener moderadores para r/{subreddit.display_name} (probablemente privado).")
                    active_users_sample = []
                else:
                    raise
            except Exception as mod_error:
                logger.error(f"Error obteniendo moderadores para r/{subreddit.display_name}: {mod_error}")
                active_users_sample = []

            activity_score = random.randint(30, 90)
            relevance_score = random.randint(40, 95)
            logger.debug(
                f"r/{subreddit.display_name} - Suscriptores: {subreddit.subscribers}, Placeholder Activity: {activity_score}, Relevance: {relevance_score}")

            communities.append({
                "name": subreddit.display_name,
                "size": subreddit.subscribers if hasattr(subreddit, 'subscribers') else 0,
                "description": subreddit.public_description or "Sin descripción disponible",
                "active_users": active_users_sample,
                "activity_score": activity_score,
                "relevance_score": relevance_score
            })
        logger.info(f"Encontradas {len(communities)} comunidades relacionadas.")
        return communities
    except Exception as e:
        logger.error(f"Error al obtener comunidades para '{search_tag}': {e}")
        return []

# Comparar comentarios de comunidades
async def compare_community_comments(reddit: asyncpraw.Reddit, search_tag: str, communities: list,
                                    limit_per_community: int = CONFIG["community_post_limit"]) -> Dict[str, Any]:
    if not communities:
        logger.info("No hay comunidades para comparar.")
        return {"communities": [], "summary": {}}
    try:
        comparison_data = []
        all_community_avg_post_scores = []
        all_community_avg_comments_per_post = []

        logger.info(
            f"Comparando hasta {limit_per_community} posts para '{search_tag}' en {len(communities)} comunidades...")

        tasks = []
        for community in communities:
            tasks.append(analyze_community_posts(reddit, search_tag, community, limit_per_community))

        results = await asyncio.gather(*tasks)

        for result in results:
            if result:
                comparison_data.append(result)
                all_community_avg_post_scores.append(result.get("avg_post_score", 0))
                all_community_avg_comments_per_post.append(result.get("avg_comments_per_post", 0))

        max_avg_score = max(all_community_avg_post_scores) if all_community_avg_post_scores else 1
        max_avg_comments = max(all_community_avg_comments_per_post) if all_community_avg_comments_per_post else 1

        most_active_community_obj = max(comparison_data, key=lambda x: x.get("avg_comments_per_post", 0), default=None)
        highest_scored_community_obj = max(comparison_data, key=lambda x: x.get("avg_post_score", 0), default=None)

        logger.info("Comparación de comunidades completada.")
        return {
            "communities": comparison_data,
            "summary": {
                "most_active_community": most_active_community_obj[
                    "community_name"] if most_active_community_obj else "N/A",
                "highest_scored_community": highest_scored_community_obj[
                    "community_name"] if highest_scored_community_obj else "N/A",
                "max_avg_score": max_avg_score,
                "max_avg_comments": max_avg_comments
            }
        }
    except Exception as e:
        logger.error(f"Error general al comparar comunidades: {e}")
        return {"communities": [], "summary": {}}

# Analizar posts de una comunidad
async def analyze_community_posts(reddit: asyncpraw.Reddit, search_tag: str, community: dict,
                                 limit_per_community: int) -> Optional[Dict[str, Any]]:
    subreddit_name = community.get("name")
    if not subreddit_name:
        return None

    try:
        logger.debug(f"Analizando r/{subreddit_name}...")
        subreddit = await reddit.subreddit(subreddit_name)
        posts_data_for_community = []
        community_post_scores = []
        community_post_comment_counts = []
        community_post_avg_comment_scores = []
        posts_processed_count = 0

        async for submission in subreddit.search(search_tag, limit=limit_per_community, sort="new"):
            posts_processed_count += 1
            logger.debug(f"Post '{submission.title}' tiene {submission.num_comments} comentarios")
            post_comments_summary = await get_comments(reddit, submission.id, comment_limit=10)
            avg_c_score = 0
            if post_comments_summary["comments"]:
                avg_c_score = sum(c["score"] for c in post_comments_summary["comments"]) / len(
                    post_comments_summary["comments"])

            posts_data_for_community.append({
                "post_title": submission.title,
                "post_url": f"https://www.reddit.com{submission.permalink}",
                "score": submission.score,
                "comments": post_comments_summary["comments"][:2],
                "total_comments": submission.num_comments,
            })

            community_post_scores.append(submission.score)
            community_post_comment_counts.append(submission.num_comments)
            community_post_avg_comment_scores.append(avg_c_score)

        logger.info(
            f"r/{subreddit_name}: Procesados {posts_processed_count} posts con {sum(community_post_comment_counts)} comentarios totales.")

        if posts_processed_count == 0:
            logger.warning(f"No se encontraron posts para '{search_tag}' en r/{subreddit_name}")
            return {
                "community_name": subreddit_name,
                "community_size": community.get("size", 0),
                "posts": [],
                "total_comments_in_analyzed_posts": 0,
                "avg_comment_score": 0,
                "avg_post_score": 0,
                "avg_comments_per_post": 0
            }

        avg_post_score = sum(community_post_scores) / max(1, len(community_post_scores))
        avg_comments_per_post = sum(community_post_comment_counts) / max(1, len(community_post_comment_counts))
        avg_community_comment_score = sum(community_post_avg_comment_scores) / max(1,
        len(community_post_avg_comment_scores))

        return {
            "community_name": subreddit_name,
            "community_size": community.get("size", 0),
            "posts": posts_data_for_community,
            "total_comments_in_analyzed_posts": sum(community_post_comment_counts),
            "avg_comment_score": avg_community_comment_score,
            "avg_post_score": avg_post_score,
            "avg_comments_per_post": avg_comments_per_post
        }

    except asyncpraw.exceptions.RedditAPIException as e:
        if "403" in str(e) or "FORBIDDEN" in str(e).upper():
            logger.warning(f"Acceso denegado a r/{subreddit_name} durante la comparación.")
            return None
        logger.error(f"Error analizando posts en r/{subreddit_name}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error inesperado analizando posts en r/{subreddit_name}: {e}")
        return None

# Generar reporte
async def generate_report(reddit: asyncpraw.Reddit, search_tag: str) -> Optional[str]:
    cache_key = search_tag.lower().replace(" ", "_")
    target_subreddit = "all"
    logger.info(f"Iniciando generación de reporte para '{search_tag}' en r/{target_subreddit}")

    task_event = asyncio.create_task(get_latest_event(reddit, target_subreddit, search_tag))
    print_info("Buscando post principal...")
    await search_animation(task_event)
    latest_event = await task_event

    comments_data = {"total_comments": 0, "comments": []}
    if latest_event and latest_event.get("id"):
        print_info(f"Obteniendo comentarios para post ID: {latest_event['id']}...")
        task_comments = asyncio.create_task(
            get_comments(reddit, latest_event["id"], comment_limit=CONFIG["comment_limit_timeline"]))
        await search_animation(task_comments)
        comments_data = await task_comments
    else:
        logger.warning(f"No se encontró post principal para '{search_tag}', creando placeholder.")
        latest_event = {
            "type": "post", "title": "Sin Post Principal Encontrado", "author": {"name": "N/A", "total_karma": 0},
            "created_utc": datetime.now(timezone.utc).timestamp(),
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "time_ago": "ahora",
            "body": f"No se encontró un post reciente relevante para '{search_tag}' en r/{target_subreddit}.",
            "score": 0, "url": "", "media": [], "subreddit": target_subreddit, "id": None,
            "engagement": {"upvotes": 0, "total_comments": 0, "awards": 0, "share_url": ""}
        }

    print_info("Buscando comunidades relacionadas...")
    task_communities = asyncio.create_task(get_communities(reddit, search_tag, limit=CONFIG["community_limit"]))
    await search_animation(task_communities)
    communities = await task_communities

    print_info("Comparando posts en comunidades encontradas...")
    task_comparison = asyncio.create_task(
        compare_community_comments(reddit, search_tag, communities, limit_per_community=CONFIG["community_post_limit"]))
    await search_animation(task_comparison)
    community_comparison = await task_comparison

    all_events_for_timeline = []
    if latest_event and latest_event.get("id"):
        all_events_for_timeline.append(latest_event)
    all_events_for_timeline.extend(comments_data["comments"])
    all_events_for_timeline.sort(key=lambda x: x.get('created_utc', 0), reverse=True)
    logger.info(f"Preparados {len(all_events_for_timeline)} eventos para el timeline.")

    final_report_data = {
        "tag": search_tag,
        "event": latest_event,
        "engagement": latest_event.get("engagement", {}),
        "comments": comments_data["comments"][:CONFIG["comment_limit_display"]],
        "total_comments_available": comments_data["total_comments"],
        "all_events": all_events_for_timeline,
        "communities": communities,
        "community_comparison": community_comparison,
        "sentiment": {"positive": 0, "neutral": 0, "negative": 0}
    }

    print_info("Renderizando reporte HTML...")
    template_content = verify_template(Path('report.html'), REPORT_TEMPLATE_URL)
    if not template_content:
        print_error("No se pudo obtener la plantilla del reporte.")
        return None

    try:
        template = Template(template_content)
        html_content = template.render(data=final_report_data)
        report_filename = f'report_{cache_key}_{int(datetime.now().timestamp())}.html'
        output_path = Path(report_filename).resolve()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        logger.info(f"Reporte generado: {output_path}")

        try:
            webbrowser.open(output_path.as_uri())
        except Exception as wb_error:
            logger.error(f"No se pudo abrir el reporte en el navegador automáticamente: {wb_error}")
            print(f"Reporte guardado en: {output_path}")
        return str(output_path)
    except Exception as render_error:
        logger.error(f"Error durante el renderizado de Jinja2: {render_error}")
        print_error(f"Error al generar el HTML del reporte: {render_error}")
        return None

# Scrape de análisis de usuario
async def scrape_reddit_user_analysis(username: str) -> None:
    def sync_scrape():
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 15)
        try:
            driver.get("https://reddit-user-analyser.netlify.app/")
            search_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
            search_input.send_keys(username)
            analyse_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.input-group-btn button')))
            analyse_button.click()
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.summary')))
            time.sleep(45)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            user_data = {
                'username': username,
                'joined_date': soup.select_one('.subtext strong').text.strip(),
                'comments': soup.select_one('.stat-circle--comments').get('data-value'),
                'submissions': soup.select_one('.stat-circle--submitted').get('data-value'),
                'controversial_percent': soup.select_one('.stat-circle--controversiality').get('data-value'),
                'karma_comment': soup.select_one('.stat-circle--per-comment').get('data-value'),
                'karma_submission': soup.select_one('.stat-circle--per-submission').get('data-value'),
                'top_subreddits': [
                    {'name': a.text.strip(), 'posts': a.find('small').text.strip()}
                    for a in soup.select('.card--dark a') if '/r/' in a['href']
                ][:7],
                'frequent_words': [
                    {'word': a.text.split()[0], 'count': a.find('small').text.split()[0]}
                    for a in soup.select('.card--dark a') if 'google.com' in a['href']
                ][:12]
            }
            return user_data
        except Exception as e:
            print_error(f"Error al analizar usuario {username}: {e}")
            return {'username': username, 'error': str(e)}
        finally:
            driver.quit()

    return await asyncio.to_thread(sync_scrape)

# Generar reporte de usuario
async def generate_user_report(user_data: Dict[str, Any]) -> None:
    if 'error' in user_data:
        print_error(f"No se pudo generar reporte para {user_data['username']}: {user_data['error']}")
        return

    template_content = verify_template(Path('user_report_template.html'), USER_REPORT_TEMPLATE_URL)
    if not template_content:
        return

    progress_bar()
    template = Template(template_content)
    report_filename = f'user_report_{user_data["username"]}.html'
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(template.render(user_data))

    webbrowser.open(f"file://{os.path.abspath(report_filename)}")
    print_success(f"Reporte de usuario generado: {report_filename}")

# Crear plantilla de reporte de usuario
def create_user_report_template() -> None:
    template_content = verify_template(Path('user_report_template.html'), USER_REPORT_TEMPLATE_URL)
    if template_content:
        print_success("Plantilla de reporte de usuario descargada")
    else:
        print_error("No se pudo descargar la plantilla de reporte de usuario")

# Eliminar reportes previos
def delete_previous_reports() -> None:
    report_files = glob.glob("report_*.html") + glob.glob("user_report_*.html")
    template_name = "user_report_template.html"
    files_to_delete = [f for f in report_files if Path(f).name != template_name]

    if not files_to_delete:
        logger.info("No hay reportes previos para eliminar.")
        return

    deleted_count = 0
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            logger.info(f"Reporte previo eliminado: {file_path}")
            deleted_count += 1
        except OSError as e:
            logger.error(f"Error al eliminar reporte {file_path}: {e}")
            print_error(f"No se pudo eliminar {file_path}")
    if deleted_count > 0:
        print_info(f"Se eliminaron {deleted_count} reportes previos.")

# Bucle principal
async def main() -> None:
    print_banner()

    download_choice = input(
        f"{Fore.YELLOW}¿Descargar/Actualizar plantillas desde GitHub? (s/N): {Style.RESET_ALL}").strip().lower()
    CONFIG["download_template"] = (download_choice == 's')

    create_user_report_template()
    verify_template(Path('report.html'), REPORT_TEMPLATE_URL)

    try:
        reddit = asyncpraw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
        )
    except Exception as init_error:
        logger.error(f"Error al inicializar el cliente PRAW: {init_error}", exc_info=True)
        print_error(
            "Error crítico al configurar la conexión con Reddit. Verifica las variables de entorno y la instalación de PRAW.")
        return

    if not await verify_reddit_auth(reddit):
        print_error("Fallo en la autenticación con Reddit. Verifica tus credenciales (.env) o los permisos de la app.")
        await reddit.close()
        return

    print_success("Conectado y autenticado con la API de Reddit.")

    delete_previous_reports()
    cache_dir = Path(CONFIG["cache_dir"])
    if cache_dir.exists():
        try:
            shutil.rmtree(cache_dir)
            logger.info("Directorio de caché limpiado.")
            print_info("Caché anterior limpiada.")
        except OSError as e:
            logger.error(f"Error al limpiar caché: {e}")
            print_error("No se pudo limpiar el directorio de caché.")

    while True:
        print_menu()
        choice = input(f"{Fore.YELLOW}{Style.BRIGHT}Selecciona una opción (1-3): {Style.RESET_ALL}").strip()

        if choice == '1':
            username = input(f"{Fore.CYAN}Ingresa el nombre de usuario de Reddit: {Style.RESET_ALL}").strip()
            if not username:
                print_error("Por favor, ingresa un nombre de usuario válido")
                continue
            print_info(f"Analizando usuario: {username}")
            task = asyncio.create_task(scrape_reddit_user_analysis(username))
            await search_animation(task)
            user_data = await task
            await generate_user_report(user_data)

        elif choice == '2':
            search_tag = input(f"{Fore.CYAN}Ingresa el tema a buscar en Reddit: {Style.RESET_ALL}").strip()
            if not search_tag:
                print_error("El tema no puede estar vacío.")
                continue
            search_tag_formatted = search_tag.capitalize()
            print_info(f"Iniciando análisis para el tema: '{search_tag_formatted}'")
            try:
                report_filename = await generate_report(reddit, search_tag_formatted)
                if report_filename:
                    print_success(f"Reporte generado: {report_filename}")
                else:
                    print_error(f"No se pudo generar el reporte para '{search_tag_formatted}'. Revisa el log.")
            except Exception as e:
                logger.error(f"Error inesperado al generar reporte para '{search_tag_formatted}': {e}", exc_info=True)
                print_error(f"Ocurrió un error inesperado al generar el reporte. Revisa 'reddit_analyser.log'.")

        elif choice == '3':
            print_success("Saliendo del Reddit Analyser. ¡Adiós!")
            break

        else:
            print_error("Opción inválida. Por favor, elige 1, 2 o 3.")

        print("-" * 40)

    if reddit and not reddit.read_only:
        try:
            await reddit.close()
            logger.info("Sesión de Reddit cerrada con éxito.")
            print_info("Sesión de Reddit cerrada.")
        except Exception as close_error:
            logger.error(f"Error al cerrar la sesión de Reddit: {close_error}")

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
        logger.warning("Ejecución interrumpida por KeyboardInterrupt.")
