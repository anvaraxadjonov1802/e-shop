from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Products, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','category', 'name','price')
        
        

    
