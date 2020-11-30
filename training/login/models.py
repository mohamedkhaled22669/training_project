from django.contrib.admin import autodiscover
from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    
    class Meta:
        db_table = "Member"
        
        
