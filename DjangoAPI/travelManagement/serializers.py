from dataclasses import fields

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
