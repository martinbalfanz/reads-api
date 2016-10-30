from rest_framework.permissions import IsAuthenticated
from reads.bookmarks.models import Bookmark
from reads.bookmarks.serializers import BookmarkSerializer
from rest_framework import viewsets
from django_filters.rest_framework import FilterSet


class BookmarkFilter(FilterSet):

    class Meta:
        model = Bookmark
        fields = ['shared', 'toread']


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to view or edit all bookmarks.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Bookmark.objects.all().order_by('-time')
    serializer_class = BookmarkSerializer
    filter_class = BookmarkFilter
    search_fields = ['href', 'description', 'extended', 'tags']
