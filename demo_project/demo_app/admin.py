from django.contrib import admin

# Register your models here.
from demo_app.models import *

admin.site.register(CO2data)
admin.site.register(Location)