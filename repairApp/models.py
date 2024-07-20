from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    country = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class WorkShop(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    oldtimer = models.BooleanField()
    def __str__(self):
        return self.name
class Car(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    maxSpeed = models.IntegerField()
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.type
class Repair(models.Model):
    code = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='repais/')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.code
class ManufacturerWorkShop(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)

