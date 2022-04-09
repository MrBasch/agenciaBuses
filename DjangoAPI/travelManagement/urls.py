from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views

from . import views as vista

urlpatterns = [
    # path('/', vista.index),
    path("/city", vista.CityAPI.as_view(), name="cities_view"),
    path("/station", vista.StationAPI.as_view(), name="station_view"),
    path("/route", vista.RouteAPI.as_view(), name="route_view"),
    path("/bus", vista.BusAPI.as_view(), name="bus_view"),
    path("/driver", vista.DriverAPI.as_view(), name="driver_view"),
    path("/travel", vista.TravelAPI.as_view(), name="travel_view"),
    path("/place", vista.PlaceAPI.as_view(), name="place_view"),
]
