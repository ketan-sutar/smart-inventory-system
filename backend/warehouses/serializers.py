from rest_framework import serializers
from .models import WareHouseModel


class WarehouseSerializer(serializers.ModelSerializer):
  class Meta:
    model=WareHouseModel
    fields="__all__"