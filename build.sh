set -o errexit
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_USERNAME --email=$DJANGO_SUPERUSER_EMAIL
python manage.py collectstatic --noinput
