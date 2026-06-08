from django.db import models

from django.conf import settings
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
  
  
class Inventory(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        'warehouses.WareHouseModel',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (
            "product",
            "warehouse"
        )

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name}"
    
     
      
      
      
class StockTransaction(models.Model):

    TRANSACTION_CHOICES = (
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
        ("TRANSFER", "Transfer")
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        'warehouses.WareHouseModel',
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_CHOICES
    )

    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )