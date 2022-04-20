from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User, Group
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    code = serializers.CharField(max_length=50)


class StationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    city = serializers.SerializerMethodField()

    def get_city(self, instance):
        return CitySerializer(instance.city).data


class RouteSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    stops = StationSerializer(many=True)
    name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)


class BusSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=50)


class DriverSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    rut = serializers.CharField(max_length=12)
    status = serializers.CharField(max_length=50)


class TravelSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    route = RouteSerializer()
    bus = BusSerializer()
    driver = DriverSerializer()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()


class PlaceSerializer(serializers.Serializer):
    travel = TravelSerializer()
    code = serializers.CharField(max_length=50)
    available = serializers.BooleanField()


class PassengerSerializer(serializers.Serializer):
    place = PlaceSerializer()
    name = serializers.CharField(max_length=50)
    rut = serializers.CharField(max_length=12)
