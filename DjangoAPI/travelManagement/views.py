from asyncio.windows_events import NULL
from distutils.command.upload import upload
from telnetlib import STATUS
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from isort import code
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . import serializers
from .services import get_all_stations, create_city, delete_city, get_all_cities, get_city_with_code, get_or_create_city, get_or_create_station, upload_or_create_city

# Create your views here.


class CityAPI(APIView):
    def get(self, request):
        cities = get_all_cities()
        serializer = serializers.CitySerializer(cities, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        city, created = get_or_create_city(name=name, code=code)
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if(not created):
            data["message"] = "failed to add, the city already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            city = get_city_with_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        delete_city(city=city)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.data.get("code")
        name = request.data.get("name")
        new_code = request.data.get("new_code")
        city, created = upload_or_create_city(
            name=name, code=code, new_code=new_code)
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if(created):
            data["message"] = "the city was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(data=data, status=status.HTTP_200_OK)


class StationAPI(APIView):
    def get(self, request):
        station = get_all_stations()
        serializer = serializers.StationSerializer(station, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        city = request.data.get("city")
        station, created = get_or_create_station(
            name=name, code=code, city=city)
        serializer = serializers.StationSerializer(station)
        print("station serializer = ", serializer)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if(not created):
            data["message"] = "failed to add, the station already exist"
            print("stations = ", Station.objects.all())
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)
