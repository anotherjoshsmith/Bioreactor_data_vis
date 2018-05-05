
from django.shortcuts import render
from demo_app.models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.
def locations(request):
    allLocations = Location.objects.all()

    result_list = []
    for i in allLocations:
        result = {
            "id": i.id,
            "lat": i.lat,
            "lng": i.lng,
            "station": i.station
        }
        result_list.append(result)

    return JsonResponse(result_list, safe = False )

def readings(request, location):
    location = Location.objects.get(id= location)

    raw_results = CO2data.objects.filter(location=location).all()

    result_list = []
    for i in raw_results:
        result = {
            'id': i.id,
            'co2conc': i.co2_concentration,
            'temp': i.temp,
        }
        result_list.append(result)

    return JsonResponse(result_list,safe=False)


