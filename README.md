# Onin Werx

Web Portal, Electronics, Parts

### setup environment

1. virtualenv -p /usr/local/bin/python3.7 ~/.onin
2. source ~/.onin/bin/activate
3. pip install -r requirements

### First Steps

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

Fix problems if any...

python manage runserver