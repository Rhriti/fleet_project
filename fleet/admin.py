
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Station, Vehicle

class StationResource(resources.ModelResource):
    class Meta:
        model = Station
        import_id_fields = ['station_code']
        fields = ['station_name', 'station_code', 'latitude', 'longitude', 'city', 'operating_radius']

@admin.register(Station)
class StationAdmin(ImportExportModelAdmin):
    resource_class = StationResource
    list_display = ('station_name', 'station_code', 'city', 'operating_radius')

@admin.register(Vehicle)
class VehicleAdmin(ImportExportModelAdmin):
    list_display = ('registration_number', 'vehicle_model', 'current_station', 'odometer_reading', 'fuel_level')