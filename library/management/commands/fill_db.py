import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Fills the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
