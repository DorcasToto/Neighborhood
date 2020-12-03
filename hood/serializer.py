from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Neighbourhood,Profile,Business,Post
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets



class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    neighbourhood = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model =  Business
        fields = ['businessName', 'user', 'neighbourhood', 'businessEmail']   


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

class HoodSerializer(serializers.ModelSerializer):
    business_set = BusinessSerializer(many=True)
    class Meta:
        model =  Neighbourhood
        fields = ['id', 'hoodName','photo','hoodLocation', 'occupantsCount','admin', 'business_set'] 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ['title', 'text', 'user','date','neighbourhood'] 


class ProfileSerializer(serializers.ModelSerializer):
    neighbourhood = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['name', 'idNo', 'neighbourhood', 'status', 'photo', 'user']    

        
# class BusinessSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=False)
#     neighbourhood = serializers.PrimaryKeyRelatedField(read_only=False)

#     class Meta:
#         model =  Business
#         fields = ['businessName', 'user', 'neighbourhood', 'businessEmail']