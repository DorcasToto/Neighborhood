from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, UserRegistrationSerializer,HoodSerializer,PostSerializer,ProfileSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import Profile,Neighbourhood,Business
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly

def index(request):
    return render('index.html')

class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """

    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.assigned_to == request.user: 
            return True

        return False

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

class HoodList(APIView):
    def get(self,request,format = None):
        all_hoods = Neighbourhood.objects.all()
        serializerdata = HoodSerializer(all_hoods,many = True)
        return Response(serializerdata.data)

class PostList(APIView):

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)


    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def patch(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessViewset(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAssigned, permissions.IsAdminUser]

    # def list(self, request, *args, **kwargs):
    #     self.get_queryset = Business.objects.filter(user=request.user)

    #     if request.user.is_superuser():
    #         self.get_queryset = Business.objects.all()

    #     super().list(*args, **kwargs)
