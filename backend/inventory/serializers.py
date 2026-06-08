from rest_framework import serializers
from .models import (Category, Product)



class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=Category
    fields="__all__"
    
    
class ProductSerializer(serializers.ModelSerializer):
  
  category_name=serializers.CharField(source="category.name",read_only=True)

  class Meta:
    model=Product
    fields="__all__"
    
class StockInSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    warehouse_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class TransferSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

    source_warehouse = serializers.IntegerField()

    destination_warehouse = serializers.IntegerField()

    quantity = serializers.IntegerField(min_value=1)