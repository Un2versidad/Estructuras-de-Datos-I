![image](https://github.com/user-attachments/assets/e1b1b52f-de9a-4232-ace4-62889211479a)

# 📊 Reddit Analytics - Análisis de Comunidades y Engagement 🕵️‍♂️

¡Bienvenido/a al proyecto **Reddit Analytics**! 🚀 Este script en Python te permite analizar datos de Reddit de manera asíncrona, buscar comunidades relacionadas con un tema, obtener información sobre usuarios, comentarios, métricas de engagement (upvotes, comentarios, premios), y generar informes interactivos en HTML. Todo esto con un enfoque en encontrar comunidades y perfiles con intereses similares. 🎯

---

## 📋 Descripción General

Este proyecto utiliza la API de Reddit (a través de `asyncpraw`) para analizar datos de subreddits, posts y perfiles de usuarios basados en temas o nombres de usuario. Genera informes HTML detallados con:

- 📰 **Último evento (post)** relacionado con el tema.
- 💬 **Comentarios destacados** y métricas de engagement (upvotes, comentarios totales, premios).
- 👥 **Comunidades relacionadas** con información sobre suscriptores, descripción y moderadores activos.
- 📈 **Análisis de usuarios** con estadísticas como karma, actividad en subreddits, palabras frecuentes y más.
- 🌟 **Interfaz interactiva** con animaciones y barras de progreso.

El script incluye almacenamiento en caché para mejorar el rendimiento, manejo de excepciones robusto y un diseño de informe HTML moderno y responsivo. 🌟

---

## 📸 Screenshot (Ejemplo de Resultados)

![image](https://github.com/user-attachments/assets/7e289e6a-ba15-415e-9d21-4ea3b098c44a)

![image](https://github.com/user-attachments/assets/fb96bb01-32dc-4968-aa63-08508a5dd6e5)

---

## 🎞️ Video (Ejemplo de Funcionamiento)

[Ver video](https://github.com/user-attachments/assets/55187dee-e544-4934-ac23-a15b1a1cee52)

---

## 🛠️ Requisitos

Antes de empezar, asegúrate de tener instalado lo siguiente:

- **Python 3.8+** 🐍
- Una cuenta de Reddit y credenciales de API (client_id, client_secret, etc.)
- Dependencias necesarias (instálalas con `pip`):

```bash
pip install asyncpraw jinja2 python-dotenv selenium webdriver-manager bs4 colorama
```

---

## 📂 Estructura del Proyecto

```plaintext
reddit-analytics/
│
├── Reddit_Analytics.py      # Script principal para el análisis de Reddit
├── report.html              # Plantilla Jinja2 para generar informes de temas
├── user_report_template.html # Plantilla Jinja2 para informes de usuarios
├── .env                     # Archivo para almacenar las credenciales de Reddit
├── .cache/                  # Directorio para almacenar datos en caché
└── README.md                # Este archivo con la documentación
```

---

## 🛠 Configuración

### 1. Crea un archivo `.env`

Crea un archivo `.env` en la raíz del proyecto y añade tus credenciales de Reddit. Puedes obtenerlas creando una app en [Reddit Apps](https://www.reddit.com/prefs/apps).

```plaintext
REDDIT_CLIENT_ID=tu_client_id
REDDIT_CLIENT_SECRET=tu_client_secret
REDDIT_USER_AGENT=tu_user_agent
REDDIT_USERNAME=tu_usuario
REDDIT_PASSWORD=tu_contraseña
```

### 2. Instala las dependencias

Ejecuta el siguiente comando para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, créalo con:

```plaintext
asyncpraw
jinja2
python-dotenv
selenium
webdriver-manager
bs4
colorama
```

---

## 🚀 Uso

### Ejecuta el script principal

Corre el script `Reddit_Analytics.py` desde la terminal:

```bash
python Reddit_Analytics.py
```

### Introduce una opción del menú

El programa mostrará un menú interactivo con las siguientes opciones:

1. **Analizar un usuario de Reddit**: Ingresa el nombre de un usuario para obtener estadísticas detalladas sobre su actividad.
2. **Buscar un tema**: Ingresa un tema para buscar posts relacionados, comentarios y comunidades.
3. **Salir**: Termina el programa.

### Obtén el informe generado

El script generará un archivo HTML (e.g., `report_programación_1698765432.html` o `user_report_username.html`) con el análisis completo. Ábrelo en tu navegador para ver los resultados. 🌐

---

## 🌟 Características Principales

- **Análisis Asíncrono ⚡**: Utiliza `asyncpraw` para realizar solicitudes a la API de Reddit de forma eficiente.
- **Caching 💾**: Almacena datos en caché en el directorio `.cache/` para evitar solicitudes redundantes.
- **Generación de Informes 📜**: Crea informes HTML interactivos usando Jinja2 con un diseño moderno y responsivo.
- **Manejo de Medios 🖼️**: Detecta y muestra imágenes, videos y galerías en los posts.
- **Métricas de Engagement 📊**: Calcula upvotes, comentarios totales, premios y ratios de interacción.
- **Análisis de Usuarios 🧑‍💻**: Obtiene estadísticas detalladas sobre usuarios utilizando web scraping.
- **Búsqueda de Comunidades 👥**: Encuentra comunidades relacionadas y sus moderadores activos.
- **Interfaz Interactiva ✨**: Animaciones y barras de progreso para mejorar la experiencia del usuario.

---

## 🧠 Estructuras de Datos Utilizadas y Razonamiento

El script utiliza varias estructuras de datos para manejar y procesar la información de Reddit. Aquí te explico las principales y por qué se eligieron:

### 1. Diccionarios (`dict`)

**Uso**: Almacenar datos de posts, comentarios, comunidades, usuarios y métricas de engagement.  
**Razonamiento**: Los diccionarios son ideales para representar datos estructurados con claves significativas (e.g., `title`, `author`, `score`). Son flexibles y permiten acceder rápidamente a los datos mediante claves.

**Ejemplo**:
```python
latest_event = {
    "title": "Un post interesante",
    "author": {"name": "usuario", "post_karma": 1000},
    "score": 500,
    "media": [{"type": "image", "url": "example.com"}]
}
```

### 2. Listas (`list`)

**Uso**: Almacenar colecciones de comentarios, comunidades y medios (imágenes/videos).  
**Razonamiento**: Las listas son perfectas para manejar colecciones ordenadas de datos, como una lista de comentarios o imágenes en un post.

**Ejemplo**:
```python
comments = [
    {"user": {"name": "user1"}, "body": "Gran post!", "score": 10},
    {"user": {"name": "user2"}, "body": "Me gusta!", "score": 5}
]
```

### 3. Archivos JSON para Caché

**Uso**: Guardar datos obtenidos de Reddit en archivos JSON dentro del directorio `.cache/`.  
**Razonamiento**: JSON es un formato ligero y fácil de leer/escribir. Permite almacenar datos complejos (diccionarios y listas) de forma persistente y recargarlos rápidamente.

---

## 📈 Ejemplo de Salida

Un informe generado (`report_programación_1698765432.html`) podría incluir:

- **Último Post**: "¡Aprende Python en 30 días!" de r/programming.
- **Métricas**: 1200 upvotes, 300 comentarios, 5 premios.
- **Comentarios**: Lista de 9 comentarios destacados con usuarios y puntuaciones.
- **Comunidades**: r/learnpython, r/python, etc., con suscriptores y moderadores.

Un informe de usuario (`user_report_username.html`) podría incluir:

- **Fecha de Registro**: 2015-03-15
- **Estadísticas**: 500 comentarios, 200 envíos, 15% controversia.
- **Subreddits Activos**: r/programming, r/python, etc.
- **Palabras Frecuentes**: "code", "project", "help".

---

## ⚠️ Notas y Limitaciones

- **Límites de la API**: Reddit impone límites de solicitudes. El script usa caché para mitigar esto.
- **Credenciales**: Asegúrate de que tus credenciales en `.env` sean correctas.
- **Errores de Red**: El script maneja excepciones, pero una conexión inestable puede afectar los resultados.
- **Web Scraping**: El análisis de usuarios depende de un sitio externo (`reddit-user-analyser.netlify.app`). Si este sitio cambia su estructura o deja de funcionar, la funcionalidad podría verse afectada.

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo y modificarlo como desees. 📄

---

## 🌟 Agradecimientos

- A `asyncpraw` por facilitar el acceso a la API de Reddit.
- A `Jinja2` por permitir la generación de informes HTML dinámicos.
- A la comunidad de Reddit por ser una fuente infinita de datos interesantes. 😎
