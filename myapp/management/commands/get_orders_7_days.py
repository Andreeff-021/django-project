from django.core.management.base import BaseCommand
from myapp.models import Order, User, Product
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('user_pk', type=int, help='User ID')
        parser.add_argument('count_day', type=int, help='Time')

    def handle(self, *args, **kwargs):
        user_pk = kwargs['user_pk']
        count_day = kwargs['count_day']
        last_day = datetime.now() - timedelta(days=count_day)
        print(last_day)
        user = User.objects.filter(pk=user_pk).first()
        orders = Order.objects.filter(customer_id=user, date_ordered__gte=last_day)
        products = set()
        for order in orders:
            for product in order.products.all():
                products.add(product)
        for product in products:
            self.stdout.write(f'{product}')