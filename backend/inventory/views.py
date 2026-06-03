from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import(Category,Product)
from .serializers import (CategorySerializer,ProductSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer
  
class ProductViewSet(viewsets.ModelViewSet):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer