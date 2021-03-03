from django.db import models

# Create your models here. name, rating, price, discount, brand, color
class App(models.Model):
    name = models.CharField(max_length=30, blank=False,default='')
    rating = models.FloatField(max_length=70, blank=False, default='')
    price = models.FloatField(max_length=200,blank=False, default='')
    discount = models.FloatField(default=False)
    brand = models.CharField(max_length=70, blank=False, default='')
    color = models.CharField(max_length=200,blank=False, default='')
