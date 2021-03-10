from django.db import models
# Create your models here.

class Storage(models.Model):
    name = models.CharField(max_length=200,db_index=True)

class Truck(models.Model):
    name = models.CharField(max_length=200,db_index=True)


