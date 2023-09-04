from datetime import datetime
from django.core.management.base import BaseCommand
from sem2_app.models import Author


class Command(BaseCommand):
    help = 'Create author'

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(name=f'name_{i}', surname=f'surname_{i}', email=f'email_{i}mail.ru',
                            biography=f'bal_bla_bla')
            author.save()
        self.stdout.write('author created')
