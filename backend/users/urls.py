from django.urls import path
from .views import ResgiterView

urlpatterns = [
    path('register/', ResgiterView.as_view(), name='register'),
]