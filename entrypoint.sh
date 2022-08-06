# Установка библиотек
python install -r requirements.txt


# Миграции
python app/manage.py makemigrations users
python app/manage.py migrate users

python app/manage.py makemigrations app
python app/manage.py migrate app

python app/manage.py makemigrations
python app/manage.py migrate


# Создание аминистратор
python app/manage.py createsuperuser