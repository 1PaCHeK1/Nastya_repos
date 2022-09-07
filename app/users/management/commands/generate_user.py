from django.core.management.base import BaseCommand

from users.models import User

import os, json


class Command(BaseCommand):
    help = "Создание пользователей"
    
    def handle(self, *args, **options):
        with open(os.path.join(
                    os.path.abspath(
                    os.path.dirname(__file__)
                  ), 
                  'user_data.json'), 'rb') as f:
            data = json.loads(f.read())

        for user in data:
            user_qs = User.objects.filter(username=user['username'])
            if not user_qs.exists():
                print(f"Generate user with username '{user['username']}'")
                User.objects.create(**user)
            else:
                print(f"User with username '{user['username']}' already exists")
                