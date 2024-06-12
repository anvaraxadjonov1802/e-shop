from enum import unique
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The email must be set"))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    
    email = models.CharField(max_length = 100, unique = True)
    phone = models.CharField(max_length = 100, unique = True, null=True)   
    username = None
    first_name = models.CharField(max_length = 255, blank = True, null = True)
    last_name = models.CharField(max_length = 255, blank = True, null = True)
    password = models.CharField(max_length = 255)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    modeified = models.DateTimeField(auto_now = True)
    is_email_verified = models.BooleanField(default = False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
class CodeConfirmation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_code')
    code = models.IntegerField()
    code_token = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return f'{self.user}----{self.code}'