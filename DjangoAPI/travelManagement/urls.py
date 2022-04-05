from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views

from . import views as vista

urlpatterns = [
    # path('/', vista.index),
    path("/city", vista.CityAPI.as_view(), name="cities_view"),
]
