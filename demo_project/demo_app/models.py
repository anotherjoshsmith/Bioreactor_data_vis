from django.db import models

# Create your models here.
class CO2data(models.Model):#defining class and inhereting models.Model (wheel in a car, a class)
    date_time = models.DateTimeField()
    co2_concentration = models.DecimalField(max_digits=5, decimal_places=1)
    temp = models.DecimalField(max_digits=4, decimal_places=1)

