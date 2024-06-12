from email import message
import email
from pickle import TRUE
from sre_constants import SUCCESS
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import CustomUser, CustomUserManager, CodeConfirmation
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from helpers.generatorcode import generate_code, generate_code_token
from helpers.smssender import send_email
 

class RegisterAPIView(APIView):
    # permission_class = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        
        ex_user = CustomUser.objects.filter(email=email).first()
        if ex_user:
            return Response({'massage' : 'Bu Email tizimda mavjud'})
        user = CustomUser.objects.create_user(
            email = email,
            phone = phone, 
            first_name = first_name,
            last_name = last_name,
            password = make_password(password),
            is_active = True
        )
        
        token = RefreshToken.for_user(user=user)
        return Response(
            {
                'massage' : 'Success',
                'user_info': UserSerializer(user).data,
                'access_token' : str(token.access_token),
                'refres_token' : str(token)
            }
        )
            

class LoginAPIView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        print(email)
        ex_user = CustomUser.objects.filter(email=email).first()
        
        if not ex_user:
            return Response({'massage' : 'Bu Email tizimda mavjud emas'})
        
        code = generate_code(5)
        code_token = generate_code_token(32)
        sms = send_email(code, email)
        
        Confirmation = CodeConfirmation.objects.create(
            user = ex_user,
            code = code,
            code_token = code_token
        )
        
        
        return Response(
            {
                'message':str(sms['message']),                
                "Code" : str(code_token)
            }
        )
        
class LoginEndAPIView(APIView):
    def post(self, request):
        code = int(request.data.get('code'))
        code_token = request.data.get('code_token')
        
        confir_user = CodeConfirmation.objects.filter(code=code, code_token=code_token).first()
        
        if not confir_user:
            return Response({'massage' : 'Bu Code xato'})
        
        confir_user.delete()
       
        token = RefreshToken.for_user(user=confir_user.user)
        return Response({
            'massage' : 'Success',
            'code_token' : str(confir_user.code_token),
            'access_token' : str(token.access_token),
            'refres_token' : str(token)
        })
        
            
        
