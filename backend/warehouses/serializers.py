from rest_framework import serializers
from .model import WareHouseModel


class WarehouseSerializer(serializers.ModelSerializer):
  class Meta:
    model=WareHouseModel
    fields="__all__"