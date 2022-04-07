from dataclasses import fields
from unittest.util import _MAX_LENGTH

from rest_framework import serializers

from travelManagement.models import (
    Bus,
    City,
    Driver,
    Passenger,
    Place,
    Route,
    Station,
    Travel,
)


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    code = serializers.CharField(max_length=50)


class StationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.SerializerMethodField()

    def get_city(self, instance):
        return CitySerializer(instance.city).data


class RouteSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    stops = StationSerializer(many=True)
    name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
