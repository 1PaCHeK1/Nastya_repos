from django.core.management.base import BaseCommand

from petstore.models import ProductType

import os, json


class Command(BaseCommand):
    help = "Создание категорий"
    
    def handle(self, *args, **options):
        with open(os.path.join(
                    os.path.abspath(
                    os.path.dirname(__file__)
                  ), 
                  'producttype_data.json'), 'rb') as f:
            data = json.loads(f.read())

        for producttype in data:
            producttype_qs = ProductType.objects.filter(type=producttype['type'])
            if not producttype_qs.exists():
                print(f"Generate product type with name '{producttype['type']}'")
                ProductType.objects.create(**producttype)
            else:
                print(f"Product type with name '{producttype['type']}' already exists")
                