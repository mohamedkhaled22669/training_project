from django.db import models

# Create your models here.

class Nodes(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=80)
    content = models.CharField(max_length=250)
    id_user = models.IntegerField()
    
    class Meta:
        db_table = "Nodes"