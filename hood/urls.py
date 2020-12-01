from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)

user_signup = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_login = UserViewSet.as_view({
    'get': 'list',
    'post': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('index',views.index),
    path('auth/signup/', user_signup, name='user_signup'),
    path('auth/login/', user_login, name='user_login'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)