from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductsAPIView.as_view() ),
    path('<int:id>', ProductsAPIView.as_view() ),
    # path('create/', ProductsAPIView.as_view() ),
    # path('update/<int:id>', ProductsAPIView.as_view() ),
    # path('delete/', ProductsAPIView.as_view() ),
    
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:id>', CategoryAPIView.as_view() ),
    # path('category/create/', CategoryAPIView.as_view() ),
    # path('category/update/<int:id>', CategoryAPIView.as_view() ),
    # path('category/delete/', CategoryAPIView.as_view() ),
]