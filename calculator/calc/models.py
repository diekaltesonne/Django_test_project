from django.db import models
# from django.contrib.gis.db import models as geo_model
# Create your models here.

class Truck(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    model = models.CharField(max_length=200,db_index=True)
    carrying_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    max_carrying_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_SiO2 = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_Fe = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'truck'
        verbose_name_plural = 'trucks'
        
    
    def __str__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_SiO2 = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_Fe = models.DecimalField(max_digits=10, decimal_places=2)
    
    # TO DO
    # WKT format
    #mpoly = models.MultiPolygonField(srid=4326, null=False, blank=False)

    class Meta:
        verbose_name = 'storage'
        verbose_name_plural = 'storages'
    
    def __str__(self):
        return self.name




