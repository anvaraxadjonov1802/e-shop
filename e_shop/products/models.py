from enum import unique
from tokenize import blank_re
from turtle import mode
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField( max_length = 100, null = True, blank = True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_product')
    price = models.DecimalField(max_digits=9, decimal_places = 0)
    stock = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self) :
        return f'{self.name} --- {self.category}'