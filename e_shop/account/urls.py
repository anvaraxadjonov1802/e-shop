from .views import RegisterAPIView, LoginAPIView, LoginEndAPIView
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path("login/",  LoginAPIView.as_view()),
    path("loginend/",  LoginEndAPIView.as_view()),
]