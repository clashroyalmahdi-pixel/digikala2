set -o errexit

# نصب پکیج‌ها
pip install -r requirements.txt

# اعمال مهاجرت‌ها
python manage.py migrate

# ایجاد سوپر یوزر با استفاده از متغیرهای محیطی
python manage.py createsuperuser --noinput --username=$DJANGO_SUPERUSER_USERNAME --email=$DJANGO_SUPERUSER_EMAIL

# تنظیم رمز عبور برای سوپر یوزر
python manage.py shell -c "
from django.contrib.auth.models import User;
user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME');
user.set_password('$DJANGO_SUPERUSER_PASSWORD');
user.save()
"

# جمع‌آوری استاتیک فایل‌ها
python manage.py collectstatic --noinput
