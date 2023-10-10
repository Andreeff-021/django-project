from django.core.management.base import BaseCommand
from myapp.models import Order, User


class Command(BaseCommand):
    help = "Get user orders by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        orders = Order.objects.filter(customer_id=pk)
        for order in orders:
            self.stdout.write(f'Заказ № {order.id}')
            for product in order.products.all():
                self.stdout.write(f'{product}\n')