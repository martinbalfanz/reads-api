from reads.bookmarks.models import Bookmark
from rest_framework import viewsets
from reads.bookmarks.serializers import BookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit all bookmarks.
    """
    queryset = Bookmark.objects.all().order_by('-time')
    serializer_class = BookmarkSerializer
