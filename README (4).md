# Day2 — News Aggregator (Django)

Developer-focused setup guide for the **Day2-NewsAggregator** repository.

> Note: I wasn’t able to fetch your repo contents directly from GitHub in this environment (network access to GitHub is blocked), so this README is written to match a **typical Django + NewsAPI news aggregator** project. If you paste your folder tree / `requirements.txt` / `settings.py` snippets, I can tighten this to be 100% exact (commands, env vars, apps, routes).

---

## What this project does

A simple Django web app that aggregates news articles using a third‑party News API (commonly **NewsAPI.org**). Typical features:
- Browse top headlines
- Filter by category/source
- Search by keyword
- Render results in Django templates

---

## Tech stack (expected)

- Python 3.10+ (works with 3.9+ in most cases)
- Django 4.x/5.x
- `requests` (or similar HTTP client)
- News API provider (e.g., NewsAPI.org)

---

## Local setup

### 1) Clone
```bash
git clone https://github.com/Mathurdanduprolu/Day2-NewsAggregator.git
cd Day2-NewsAggregator
```

### 2) Create and activate a virtual environment
**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
If you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

If not, install the usual basics:
```bash
pip install django requests python-dotenv
```

---

## Configuration (environment variables)

Create a `.env` file in the project root:

```env
# Django
DJANGO_SECRET_KEY=replace-me
DJANGO_DEBUG=true
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

# News API
NEWS_API_KEY=replace-me
NEWS_API_BASE_URL=https://newsapi.org/v2
```

### Where these are used
- `NEWS_API_KEY`: used when calling the news endpoint
- `DJANGO_SECRET_KEY`: Django security
- `DJANGO_DEBUG`: local debug mode
- `DJANGO_ALLOWED_HOSTS`: required when DEBUG is false

If you’re not using `python-dotenv`, set these in your shell instead.

---

## Run the app

### 1) Migrate
```bash
python manage.py migrate
```

### 2) Create an admin user (optional)
```bash
python manage.py createsuperuser
```

### 3) Start the server
```bash
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/

---

## Common project structure (expected)

You’ll typically see something like:

```
Day2-NewsAggregator/
  manage.py
  <project_name>/
    settings.py
    urls.py
    wsgi.py
  <app_name>/
    views.py
    urls.py
    templates/
    static/
  requirements.txt
  .env (local only, do not commit)
```

---

## How the News API call usually works

Most Django implementations do something like:

- Build a URL:
  - `GET /v2/top-headlines?country=us&apiKey=...`
  - or `GET /v2/everything?q=<keyword>&apiKey=...`
- Call it using `requests.get(...)`
- Parse JSON and render template

If your repo contains a service/helper module (recommended), it might look like:
- `news/services.py` or `utils/news_client.py`

---

## Tests (if present)

If you have tests:
```bash
python manage.py test
```

If not, recommended minimal test commands:
```bash
pip install pytest pytest-django
pytest
```

---

## Lint / format (recommended)

```bash
pip install ruff black
ruff check .
black .
```

---

## Troubleshooting

### 1) `ModuleNotFoundError: No module named 'django'`
You’re not in the venv, or requirements not installed:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) News API returns 401 / 403
- `NEWS_API_KEY` is missing or invalid
- Your free tier may block some endpoints (depends on provider)

### 3) `Invalid HTTP_HOST header`
Add your host to `ALLOWED_HOSTS` (or set env var):
```env
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Security notes

- Never commit `.env`
- Rotate `DJANGO_SECRET_KEY` and `NEWS_API_KEY` if exposed
- Keep `DEBUG=false` in production

---

## Deployment (quick notes)

Common options:
- Render / Railway / Fly.io (Django + gunicorn)
- AWS (EC2 + nginx + gunicorn) or Elastic Beanstalk

Typical production dependencies:
```bash
pip install gunicorn whitenoise
```

---

## License

Add a license if you want others to reuse your code (MIT is a common default).

---

## Maintainer

Mathur Danduprolu
