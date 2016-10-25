from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from reads.bookmarks import views


router = routers.DefaultRouter()
router.register(r'bookmarks', views.BookmarkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
