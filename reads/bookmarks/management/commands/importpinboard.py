from django.core.management.base import BaseCommand
from reads.bookmarks.models import Bookmark
import json


class Command(BaseCommand):
    help = 'Import pinboard json export into database'

    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        with open(options['file']) as fobj:
            data = json.load(fobj)
            Bookmark.objects.bulk_create([Bookmark(**x) for x in data])

        print("done.")
