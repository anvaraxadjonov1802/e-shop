from itertools import product
from math import prod
from re import search
from unicodedata import category
from urllib import response
from .serializers import *
from .models import Products, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.tokens import RefreshToken



class ProductsAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        category = request.data.get('category')
        price = request.data.get('price')
        stock = request.data.get('stock')
        
        ex_product = Products.objects.filter(name=name).first()
        ex_category = Category.objects.filter(name=category).first()
        
        if ex_product:
            return Response({'massage' : 'Bu Mahsulot tizimda mavjud'})
        if not ex_category:
            return Response({'massage' : 'Bunday Categoriya mavjud emas iltimos boshqa categoriyani kiriting yoki yangi Categoriya yarating'})
        
        product = Products.objects.create(
            name = name,
            description = description, 
            category = ex_category,
            price = price,
            stock = stock
        )
        
        return Response(
            {
                'massage' : 'Success',
            }
        )
    
    def put(self,request,id):
        name = request.data.get('name')
        description = request.data.get('description')
        category = request.data.get('category')
        price = request.data.get('price')
        stock = request.data.get('stock')
        product = Products.objects.filter(id=id).first()
        
        if product is None:
            response_data = {"response":"Bu Mahsulot Serverda Mavjud Emas"}
            return Response(response_data)
        ex_category = Category.objects.filter(name=category).first()
        if not ex_category:
            return Response({'massage' : 'Bunday Categoriya mavjud emas iltimos boshqa categoriyani kiriting yoki yangi Categoriya yarating'})
        
        
        product.name = name
        product.description = description
        product.category = ex_category
        product.stock = stock
        product.price = price
        product.save()
        
        response_data = {"response":"Success"}
        return Response(response_data)
    
    def delete(self, request):
        id = request.data.get('id')
        product = Products.objects.filter(id=id).first()
        if product is None:
            response_data = {"massage" : "Bunday id dagi muhsulot serverda mavjud emas"}
            return Response({
                "massage" : response_data
            })
        product.delete()
        response_data = {'massage' : "Mahsulot serverda o'chirildi"}
        return Response(response_data)
    
    
    def get(self, request, id=0):
        product = Products.objects.all()
        response = ProductsSerializer(product, many = True).data
        if product:   
            if id != 0:
                product2 = Products.objects.filter(id=id).first()
                response2 = ProductsSerializer(product2).data
                if product2: 
                    return Response({
                        "massage" : response2
                    })
                return Response({
                    'massage' : 'Bunday id dagi Mahsulot mavjud emas'
                })
            return Response({
                "massage" : response
            })
        return Response({
            'massage' : "Serverda Hech Qanday Mahulotlar Mavjud Emas"
        })
       
class CategoryAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
                
        category = Category.objects.create(
            name = name,
        )
        
        return Response(
            {
                'massage' : 'Success',
            }
        )
    def get(self, request, id=0):
        category = Category.objects.all()
        response_data = CategorySerializer(category, many = True).data
        if category:   
            if id != 0:
                category2 = Category.objects.filter(id=id).first()
                response2_data = CategorySerializer(category2).data
                if category2: 
                    return Response({
                        "massage" : response2_data
                    })
                return Response({
                    'massage' : 'Bunday id dagi Categoriya mavjud emas'
                })
            return Response({
                "massage" : response_data
            })
        return Response({
            'massage' : "Serverda Hech Qanday Categoriya Mavjud Emas"
        })
        
    def put(self,request,id):
        name = request.data.get('name')
        category = Category.objects.filter(id=id).first()
        
        if category is None:
            response_data = {"response":"Bu Categoriya Serverda Mavjud Emas"}
            return Response(response_data)    
        
        category.name = name
        category.save()
        response_data = {"response":"Success"}
        
        return Response(response_data)
    
    def delete(self, request):
        id = request.data.get('id')
        category = Category.objects.filter(id=id).first()
        if category is None:
            response_data = {"massage" : "Bunday id dagi Categoriya serverda mavjud emas"}
            return Response({
                "massage" : response_data
            })
        category.delete()
        response_data = {'massage' : "Categoriya serverda o'chirildi"}
        return Response(response_data)

