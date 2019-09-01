from django.core.management.base import BaseCommand, CommandError
from product.models import Color


class Command(BaseCommand):
    help = 'create colors'

    def handle(self, *args, **kwargs):
        colors = ['Black', 'White', 'Red', 'Silver', 'Yellow', 'Burgundry', 'Blue']

        for color in colors:
            Color.objects.create(name=color)
        print('Created colors')