from django.shortcuts import render
from rest_framework.generics import CreateAPIView
# Create your views here.
from .serializers import RegisterSerializer


class ResgiterView(CreateAPIView):
    serializer_class = RegisterSerializer