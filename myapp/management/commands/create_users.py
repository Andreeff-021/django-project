from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create users."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(username=f'User_{i}',
                        email=f'email_{i}@mail.com',
                        phone=f'phone_{i}',
                        address=f'Adress_{i}',
                        )
            user.save()
            self.stdout.write(f'{user}')
