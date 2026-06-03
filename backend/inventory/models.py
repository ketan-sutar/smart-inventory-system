from django.db import models

# Create your models here.

class Category(models.Model):
  name=models.CharField(max_length=100,unique=True)
  
  description=models.TextField(blank=True,null=True)
  
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name
  

class Product(models.Model):
  name=models.CharField(max_length=255)
  
  sku=models.CharField(max_length=100,unique=True)
  
  category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
  
  description=models.TextField(blank=True,null=True)
  
  price=models.DecimalField(max_digits=10,decimal_places=2)
  
  minimum_stock_level=models.IntegerField(default=10)
  
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name