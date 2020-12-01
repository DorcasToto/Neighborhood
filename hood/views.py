from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

def index(request):
    return render('index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
