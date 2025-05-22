
from django.shortcuts import render
from .models import Station, Vehicle
import json

def fleet_map(request):
   
    stations = Station.objects.all().values('station_name', 'latitude', 'longitude', 'operating_radius')  
    vehicles = Vehicle.objects.select_related('current_station').all()
 
    for vehicle in vehicles:
        vehicle.check_safety()
    
    vehicles_data = [
        {
            'registration_number': vehicle.registration_number,
            'latitude': vehicle.latitude,
            'longitude': vehicle.longitude,
            'is_unsafe': vehicle.is_unsafe
        }
        for vehicle in vehicles
    ]
    
    print(json.dumps(list(stations)))
    print(json.dumps(vehicles_data))
    return render(request, 'fleet/map.html', {
        'stations': json.dumps(list(stations)),
        'vehicles': json.dumps(vehicles_data),
    })

def home(request):
    return render(request, 'fleet/home.html')