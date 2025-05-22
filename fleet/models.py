from django.db import models

from django.db import models
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_code = models.CharField(max_length=20, unique=True,primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=50)
    operating_radius = models.FloatField()  # In kilometers

    def __str__(self):
        return f"{self.station_name} ({self.station_code})"

    # class Meta:
    #     verbose_name = "Station"
    #     verbose_name_plural = "Stations"

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    vehicle_model = models.CharField(max_length=50)
    current_station = models.ForeignKey(
        Station, 
        to_field='station_code',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="vehicles"
    )
    odometer_reading = models.FloatField()
    fuel_level = models.FloatField()  # Percentage (0-100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_unsafe = models.BooleanField(default=False)  # To mark vehicles outside radius

    def check_safety(self):
        if self.current_station:
            distance = haversine_distance(
                self.latitude, self.longitude,
                self.current_station.latitude, self.current_station.longitude
            )
            self.is_unsafe = distance > self.current_station.operating_radius
        else:
            self.is_unsafe = True  # Unsafe if no station assigned
        self.save()

    def __str__(self):
        return f"{self.vehicle_model} ({self.registration_number})"

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"