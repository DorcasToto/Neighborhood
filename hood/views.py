from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, UserRegistrationSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# Create your views here.

def index(request):
    return render('index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = permissions.IsAuthenticated

    # @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    # def create(self, request):
    #     super().create(request)
    #     # Validating our serializer from the UserRegistrationSerializer
    #     serializer = UserRegistrationSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     # Everything's valid, so send it to the UserSerializer
    #     model_serializer = UserSerializer(data=serializer.data)
    #     model_serializer.is_valid(raise_exception=True)
    #     model_serializer.save()
    #     return Response(model_serializer.data)