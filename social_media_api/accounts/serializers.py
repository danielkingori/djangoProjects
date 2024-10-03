from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import CustomUser

#user reg serializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            # profile_picture=validated_data('profile_picture'),
            
        )
        return user

#user login serializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
    
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        
        token, created = Token.objects.get_or_create(user=user)
        return {'user':user, 'token':token.key}
        