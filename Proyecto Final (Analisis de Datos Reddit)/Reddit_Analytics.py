import asyncio
import asyncpraw
import requests
from datetime import datetime
from jinja2 import Template
from pathlib import Path
from dotenv import load_dotenv
import os
import logging
import json
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
    "cache_dir": ".cache"
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
    try:
        response = requests.get(template_url, timeout=5)
        response.raise_for_status()
        github_content = response.text
        logger.info(f"Descargando plantilla {template_path} desde GitHub.")
        print_info(f"Descargando plantilla {template_path.name} desde GitHub.")
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(github_content)
        return github_content
    except requests.RequestException as e:
        logger.error(f"No se pudo descargar la plantilla desde GitHub: {e}")
        if template_path.exists():
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        print_error(f"No se pudo descargar la plantilla: {e}")
        return None

# Autenticación de Reddit
async def verify_reddit_auth(reddit: asyncpraw.Reddit) -> bool:
    try:
        user = await reddit.user.me()
        logger.info(f"Autenticado como: {user.name}")
        return True
    except Exception as e:
        logger.error(f"Fallo en la autenticación: {e}")
        return False

# Funciones de Caché
def load_cache(search_tag: str) -> Optional[Dict[str, Any]]:
    cache_file = Path(CONFIG["cache_dir"]) / f"{search_tag.replace(' ', '_')}.json"
    if not cache_file.exists():
        return None
    with open(cache_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_cache(search_tag: str, data: dict) -> None:
    cache_file = Path(CONFIG["cache_dir"]) / f"{search_tag.replace(' ', '_')}.json"
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    with open(cache_file, 'w', encoding='utf-8') as f:
        f.write(json_str)

# Obtención de Datos de Reddit
async def get_user_info(reddit: asyncpraw.Reddit, user: Any) -> Dict[str, Any]:
    try:
        if not user or not hasattr(user, 'name') or user.name is None:
            return {"name": "Desconocido", "post_karma": 0, "comment_karma": 0}
        redditor = await reddit.redditor(user.name)
        await redditor.load()
        return {
            "name": redditor.name,
            "post_karma": getattr(redditor, 'link_karma', 0),
            "comment_karma": getattr(redditor, 'comment_karma', 0)
        }
    except Exception as e:
        logger.warning(f"Información del usuario no disponible: {e}")
        return {"name": "Desconocido", "post_karma": 0, "comment_karma": 0}

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

async def get_comments(reddit: asyncpraw.Reddit, submission_id: str, comment_limit: int = 20) -> Dict[str, Any]:
    try:
        submission = await reddit.submission(id=submission_id)
        await submission.load()
        await submission.comments.replace_more(limit=None)
        comments = [
            {
                "user": await get_user_info(reddit, comment.author),
                "body": comment.body,
                "score": comment.score
            }
            for comment in submission.comments.list()[:comment_limit]
            if hasattr(comment, 'body') and comment.body not in ("[eliminado]", "[removido]")
        ]
        return {"total_comments": submission.num_comments, "comments": comments}
    except Exception as e:
        logger.error(f"Error al obtener comentarios: {e}")
        return {"total_comments": 0, "comments": []}

async def get_communities(reddit: asyncpraw.Reddit, search_tag: str, limit: int = CONFIG["community_limit"]) -> list:
    try:
        communities = []
        async for subreddit in reddit.subreddits.search(search_tag, limit=limit):
            moderators = [await get_user_info(reddit, mod) for mod in (await subreddit.moderator())[:3]]
            communities.append({
                "name": subreddit.display_name,
                "size": subreddit.subscribers,
                "description": subreddit.public_description or "Sin descripción disponible",
                "active_users": moderators
            })
        return communities
    except Exception as e:
        logger.error(f"Error al obtener comunidades: {e}")
        return []

# Generación de Reportes
async def generate_report(reddit: asyncpraw.Reddit, search_tag: str) -> Optional[str]:
    cache_key = search_tag.lower().replace(" ", "_")
    subreddit = await reddit.subreddit("all")

    task = asyncio.create_task(get_latest_event(reddit, subreddit.display_name, search_tag))
    await search_animation(task)
    latest_event = await task or {
        "title": "Sin datos disponibles", "author": {"name": "Desconocido"},
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "body": "Sin texto disponible", "score": 0, "url": "", "media": [], "subreddit": "all", "id": None,
        "engagement": {"upvotes": 0, "total_comments": 0, "awards": 0, "share_url": ""}
    }

    task = asyncio.create_task(get_comments(reddit, latest_event["id"]) if latest_event["id"] else asyncio.sleep(0, {
        "total_comments": 0, "comments": []}))
    await search_animation(task)
    comments_data = await task

    task = asyncio.create_task(get_communities(reddit, search_tag))
    await search_animation(task)
    communities = await task

    report_data = {
        cache_key: {
            "tag": search_tag,
            "event": latest_event,
            "engagement": latest_event["engagement"],
            "comments": comments_data["comments"],
            "communities": communities
        }
    }
    save_cache(cache_key, {"timestamp": datetime.now().isoformat(), "data": report_data})

    template_content = verify_template(Path('report.html'), REPORT_TEMPLATE_URL)
    if not template_content:
        return None

    progress_bar()
    template = Template(template_content)
    report_filename = f'report_{cache_key}_{int(datetime.now().timestamp())}.html'
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(template.render(data=report_data[cache_key]))

    webbrowser.open(f"file://{os.path.abspath(report_filename)}")
    return report_filename

async def scrape_reddit_user_analysis(username: str) -> None:
    def sync_scrape():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 10)
        try:
            driver.get("https://reddit-user-analyser.netlify.app/")
            search_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
            search_input.send_keys(username)
            analyse_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.input-group-btn button')))
            analyse_button.click()
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.summary')))
            time.sleep(30)
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

def create_user_report_template() -> None:
    template_content = verify_template(Path('user_report_template.html'), USER_REPORT_TEMPLATE_URL)
    if template_content:
        print_success("Plantilla de reporte de usuario descargada")
    else:
        print_error("No se pudo descargar la plantilla de reporte de usuario")

def delete_previous_reports() -> None:
    report_files = glob.glob("report_*.html") + [f for f in glob.glob("user_report_*.html") if f != "user_report_template.html"]
    for file in report_files:
        try:
            os.remove(file)
            logger.info(f"Reporte previo eliminado: {file}")
        except Exception as e:
            logger.error(f"Error al eliminar reporte {file}: {e}")

# Bucle Principal de CLI
async def main() -> None:
    print_banner()
    create_user_report_template()

    reddit = asyncpraw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    if not await verify_reddit_auth(reddit):
        print_error("Fallo en la autenticación. Verifica tus credenciales.")
        return

    print_success("Conectado a la API de Reddit")
    delete_previous_reports()
    cache_dir = Path(CONFIG["cache_dir"])
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
        logger.info("Directorio de caché limpiado")

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
            search_tag = input(f"{Fore.CYAN}Ingresa el tema a buscar: {Style.RESET_ALL}").strip().capitalize()
            if not search_tag:
                print_error("Por favor, ingresa un tema válido")
                continue
            print_info(f"Buscando tema: {search_tag}")
            try:
                report_filename = await generate_report(reddit, search_tag)
                if report_filename:
                    print_success(f"Reporte de tema generado: {report_filename}")
            except Exception as e:
                print_error(f"Error al generar reporte para {search_tag}: {e}")

        elif choice == '3':
            print_success("Saliendo del Reddit Analyser. ¡Adiós!")
            break

        else:
            print_error("Opción inválida. Elige 1, 2 o 3.")

    await reddit.close()
    print_info("Sesión de Reddit cerrada con éxito")

if __name__ == "__main__":
    asyncio.run(main())
