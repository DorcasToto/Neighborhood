from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)

urlpatterns = [
    path('index',views.index),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)