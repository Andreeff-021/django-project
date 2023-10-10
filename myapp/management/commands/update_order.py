from django.core.management.base import BaseCommand
from myapp.models import Order, Product


class Command(BaseCommand):
    help = "Update order name by id."

    def add_arguments(self, parser):
        parser.add_argument('order_pk', type=int, help='Order ID')
        parser.add_argument('product_pk', type=int, help='Product name')
        parser.add_argument('count', type=int, help='Products count')

    def handle(self, *args, **kwargs):
        order_pk = kwargs.get('order_pk')
        product_pk = kwargs.get('product_pk')
        count = kwargs.get('count')
        order = Order.objects.filter(pk=order_pk).first()
        product = Product.objects.filter(pk=product_pk).first()
        product.count = count
        order.products.add(product)
        order.total_price += product.price * product.count
        order.save()
        self.stdout.write(f'{order}')