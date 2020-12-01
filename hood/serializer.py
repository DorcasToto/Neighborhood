from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # password2 = serializers.CharField(
    #     required=True,
    #     style={'input_type': 'password'}
    # )
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'password', 'password2']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    # def clean_password(self):
    #     pass1 = self.validated_data['password']
    #     pass2 = self.validated_data['password2']
    #     return make_password(pass1) == make_password(pass2)

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
        