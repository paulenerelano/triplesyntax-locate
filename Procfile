web: python manage.py collectstatic --dry-run --noinput
web: gunicorn paupausiopao.wsgi -b 0.0.0.0:$PORT
