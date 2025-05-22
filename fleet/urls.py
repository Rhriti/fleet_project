from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Homepage at /
    path('map/', views.fleet_map, name='fleet_map')]