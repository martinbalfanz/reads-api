from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import FilterSet
from .models import Bookmark
from .serializers import BookmarkSerializer


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
