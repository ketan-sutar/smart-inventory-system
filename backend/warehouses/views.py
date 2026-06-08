from django.shortcuts import render

# Create your views here.
from .serializers import WarehouseSerializer
from .models import WareHouseModel

from rest_framework import viewsets


class WarehouseViewSet(viewsets.ModelViewSet):
  queryset=WareHouseModel.objects.all()
  serializer_class=WarehouseSerializer