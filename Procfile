web: gunicorn --pythonpath mysite mysite.wsgi:application
release: cd mysite && ./manage.py migrate --no-input
