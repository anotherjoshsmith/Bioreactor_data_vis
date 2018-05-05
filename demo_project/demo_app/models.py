from django.db import models

# Create your models here.
class Location(models.Model):
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    lng = models.DecimalField(max_digits=7, decimal_places=4)
    station = models.CharField(max_length=20)

class CO2data(models.Model):#defining class and inhereting models.Model (wheel in a car, a class)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    co2_concentration = models.DecimalField(max_digits=5, decimal_places=1)
    temp = models.DecimalField(max_digits=4, decimal_places=1)

