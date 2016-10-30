from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['description',
                    'time',
                    'shared',
                    'toread',
                    'tags']
    list_filter = ['time',
                   'shared',
                   'toread']
