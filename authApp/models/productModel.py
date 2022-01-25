from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=50, default=0)
    description = models.CharField('Description', max_length=200, default=0)
    category = models.CharField('Category', max_length=50, default=0)
    brand = models.CharField('Brand', max_length=50, default=0)
    sellPrice = models.FloatField(default=0)
    packaging = models.CharField('Packaging', max_length=50, default=0)
    volume = models.FloatField(default=0) #Only volume in centimeters l*w*h
    weight = models.FloatField(default=0)    
    status = models.CharField('Status', max_length=20, default=0)


