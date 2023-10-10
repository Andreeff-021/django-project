from django.core.management.base import BaseCommand
from myapp.models import Order, User, Product


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('user_pk', type=int, help='User ID')
        parser.add_argument('product_pk', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        user_pk = kwargs['user_pk']
        products_pk = kwargs['product_pk']
        user = User.objects.filter(pk=user_pk).first()
        order = Order(customer=user)
        for i in range(len(products_pk)):
            product = Product.objects.filter(pk=products_pk[i]).first()
            if order.total_price is None:
                order.total_price = product.price * product.count
            else:
                order.total_price += product.price * product.count
            order.save()
            order.products.add(product)