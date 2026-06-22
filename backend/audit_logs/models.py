from django.db import models

# Create your models here.
from django.conf import settings


class AuditLog(models.Model):
  
  ACTION_CHOICES=(
    ("CREATE","Create"),
    ("UPDATE","Update"),
    ("DELETE","Delete"),
    ("STOCK_IN","Stock In"),
    ("STOCK_OUT","Stock Out"),
    ("TRANSFER","Transfer"),
  )
  
  
  user= models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  
  action = models.CharField(
    max_length=50,
    choices=ACTION_CHOICES
  )
  
  entity=models.CharField(max_length=100)
  
  entity_id=models.IntegerField()
  
  decription = models.TextField()
  
  timestamp=models.DateTimeField(
    auto_now_add=True
  )
  
  
  def __str__(self):
    return f"{self.action} - {self.entity}"