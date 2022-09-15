from django.core.management.base import BaseCommand

from petstore.models import Product, ProductType

import os, json


class Command(BaseCommand):
    help = "Создание продуктов"
    
    def handle(self, *args, **options):
        with open(os.path.join(
                    os.path.abspath(
                    os.path.dirname(__file__)
                  ), 
                  'product_data.json'), 'rb') as f:
            data = json.loads(f.read())

        for product in data:
            product_qs = Product.objects.filter(name=product['name'])
            if not product_qs.exists():
                pt = ProductType.objects.get_or_create(type=product['type'])[0]
                print(f"Generate product with name '{product['name']}'")
                product['type'] = pt
                Product.objects.create(**product)
            else:
                print(f"Product with name '{product['name']}' already exists")
                