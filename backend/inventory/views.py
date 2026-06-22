from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import(Category,Product,Inventory,StockTransaction)
from .serializers import (CategorySerializer,ProductSerializer,StockInSerializer,TransferSerializer)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

from warehouses.models import WareHouseModel

from audit_logs.utils import create_audit_log



class CategoryViewSet(viewsets.ModelViewSet):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer
  
class ProductViewSet(viewsets.ModelViewSet):
  queryset=Product.objects.all()
  serializer_class=ProductSerializer
  
  
  
@api_view(["POST"])
def stock_in(request):
  serializer=StockInSerializer(data=request.data)
  
  serializer.is_valid(raise_exception=True)
  
  product=Product.objects.get(
    id=serializer.validated_data["product_id"]
  )
  
  warehouse=WareHouseModel.objects.get(
    id=serializer.validated_data["warehouse_id"]
  )
  
  qty=serializer.validated_data["quantity"]
  
  inventory,created=Inventory.objects.get_or_create(
    product=product,
    warehouse=warehouse
  )
  inventory.quantity+=qty
  inventory.save()
  
  StockTransaction.objects.create(
    product=product,
    warehouse=warehouse,
    quantity=qty,
    transaction_type="IN",
    performed_by=request.user
  )
  
  create_audit_log(
      user=request.user,
      action="STOCK_IN",
      entity="Product",
      entity_id=product.id,
      description=f"Added {qty} units of {product.name} to {warehouse.name}"
  )
  
  return Response({
    "message":"Stock Added Succesfully!!"
  })
  
  
@api_view(["POST"])
def stock_out(request):

    serializer = StockInSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)

    inventory = Inventory.objects.get(
        product_id=serializer.validated_data["product_id"],
        warehouse_id=serializer.validated_data["warehouse_id"]
    )

    qty = serializer.validated_data["quantity"]

    if inventory.quantity < qty:
        return Response(
            {"error": "Insufficient stock"},
            status=400
        )

    inventory.quantity -= qty
    inventory.save()

    StockTransaction.objects.create(
        product=inventory.product,
        warehouse=inventory.warehouse,
        quantity=qty,
        transaction_type="OUT",
        # performed_by=request.user
    )
    create_audit_log(
    user=request.user,
    action="STOCK_OUT",
    entity="Product",
    entity_id=inventory.product.id,
    description=f"Removed {qty} units of {inventory.product.name} from {inventory.warehouse.name}"
)

    return Response({
        "message": "Stock removed successfully"
    })
    
    
@api_view(["POST"])
def transfer_stock(request):

    serializer = TransferSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    product_id = serializer.validated_data["product_id"]
    source_id = serializer.validated_data["source_warehouse"]
    destination_id = serializer.validated_data["destination_warehouse"]
    qty = serializer.validated_data["quantity"]

    with transaction.atomic():

        source_inventory = Inventory.objects.get(
            product_id=product_id,
            warehouse_id=source_id
        )

        if source_inventory.quantity < qty:
            return Response(
                {"error": "Not enough stock"},
                status=400
            )

        destination_inventory, created = Inventory.objects.get_or_create(
            product_id=product_id,
            warehouse_id=destination_id,
            defaults={"quantity": 0}
        )

        source_inventory.quantity -= qty
        destination_inventory.quantity += qty

        source_inventory.save()
        destination_inventory.save()

        StockTransaction.objects.create(
            product_id=product_id,
            warehouse_id=source_id,
            quantity=qty,
            transaction_type="TRANSFER",
            performed_by=request.user
        )
        create_audit_log(
    user=request.user,
    action="TRANSFER",
    entity="Product",
    entity_id=product_id,
    description=f"Transferred {qty} units from Warehouse {source_id} to Warehouse {destination_id}"
)

    return Response({
        "message": "Stock transferred successfully"
    })