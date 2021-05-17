import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from library import constants
from library.models import Tale

DEFAULT_TALES_QUANTITY = 1000


class Command(BaseCommand):
    help = 'Fills the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

        parser.add_argument('--test',
                            action='store_true',
                            dest='test',
                            default=False,
                            help='Delete current content before insertion. Does not delete users.'
                            )

    def handle(self, *args, **options):
        users = User.objects.all()
        users_count = users.count()

        tales = []

        if users_count == 0:
            raise CommandError('No users in db')

        if 'tales' in options['model']:
            if options['test']:
                Tale.objects.all().delete()

            for i in range(DEFAULT_TALES_QUANTITY):
                user = users[random.randint(0, users_count - 1)]
                tales.append(Tale(title=f'TestStory{i}',
                                  content="DUMMY",
                                  genre=constants.HORROR,
                                  min_age=random.randint(0, 21),
                                  owner=user))

            Tale.objects.bulk_create(tales)
