set -o errexit
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_USERNAME --email=$DJANGO_SUPERUSER_EMAIL --password=$DJANGO_SUPERUSER_PASSWORD || true
python manage.py collectstatic --noinput
