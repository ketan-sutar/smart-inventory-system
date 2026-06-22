from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet,ProductViewSet,stock_in,stock_out,transfer_stock)

router=DefaultRouter()

router.register("categories",CategoryViewSet,basename="categories")

router.register("products",ProductViewSet,basename="products")

urlpatterns = [
  path("",include(router.urls)) ,
  path(
    "stock-in/",
    stock_in,
    name="stock-in"
  ),
  
  path(
    "stock-out/",
    stock_out,
    name="stock-out"
  ),
  
  path(
    "transfer/",
    transfer_stock,
    name="transfer-stock"
  ),
  
  
  
  
]