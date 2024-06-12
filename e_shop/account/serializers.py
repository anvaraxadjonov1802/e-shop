from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import CodeConfirmation, CustomUser, CustomUserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name']
        
class LoginStratSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        
        
class LoginEndSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()
    code_token = serializers.CharField()
    
