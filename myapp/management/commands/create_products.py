from django.core.management.base import BaseCommand
from myapp.models import Product
from random import randint


class Command(BaseCommand):
    help = "Create products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product_{i}',
                              category=randint(1, 5),
                              description=f'Description_{i}',
                              price=10,
                              quantity=randint(1, 7),
                              ratin=randint(1, 9)
                              )
            product.save()
            self.stdout.write(f'{product}')
