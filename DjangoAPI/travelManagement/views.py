from asyncio.windows_events import NULL
from distutils.command.upload import upload
from telnetlib import STATUS

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from isort import code
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import *
from .services import (
    get_city_with_code,
    delete_city,
    get_all_cities,
    get_or_create_city,
    upload_or_create_city,
    get_all_stations,
    delete_station,
    get_or_create_station,
    get_station_with_code,
    upload_or_create_station,
    get_all_routes,
    get_or_create_route,
    get_route_by_code,
    delete_route,
)

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
        if not created:
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
        city, created = upload_or_create_city(name=name, code=code, new_code=new_code)
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
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
        city_id = request.data.get("city")

        station, created = get_or_create_station(name=name, code=code, city_id=city_id)
        serializer = serializers.StationSerializer(station)
        data = {"data": serializer.data, "message": "was added succesfully"}

        if not created:
            data["message"] = "failed to add, the station already exist"
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}

        try:
            station = get_station_with_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        delete_station(station=station)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.data.get("code")
        name = request.data.get("name")
        new_code = request.data.get("new_code")
        city_id = request.data.get("city_id")
        station, created = upload_or_create_station(
            name=name, code=code, new_code=new_code, city_id=city_id
        )
        serializer = serializers.StationSerializer(station)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            data["message"] = "the station was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(data=data, status=status.HTTP_200_OK)


class RouteAPI(APIView):
    def get(self, request):
        route = get_all_routes()
        serializer = serializers.RouteSerializer(route, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     name = request.data.get("name")
    #     code = request.data.get("code")
    #     print("request post route", request.data)
    #     station_list = request.data.get("stops")
    #     print("station_list = ", station_list)
    #     print("station_list[0] = ", station_list[0])
    #     print("station_list[0] = ", type(station_list[0]))
    #     print("type = ", type(station_list))
    #     status = request.data.get("status")
    #     route, created = get_or_create_route(
    #         name=name, code=code, station_list=station_list, status=status
    #     )
    #     print("route", route)
    #     print("created", created)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            route = get_route_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE ROUTE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        delete_route(route=route)
        return Response(data=data, status=status.HTTP_200_OK)
