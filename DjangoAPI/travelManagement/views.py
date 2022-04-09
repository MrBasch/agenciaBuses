from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from isort import code
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import *
from . import services

# Create your views here.


class CityAPI(APIView):
    def get(self, request):
        cities = services.get_all_cities()
        serializer = serializers.CitySerializer(cities, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        city, created = services.get_or_create_city(name=name, code=code)
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the city already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_city(city)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            city = services.get_city_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_city(city=city)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.data.get("code")
        name = request.data.get("name")
        new_code = request.data.get("new_code")
        city, created = services.update_or_create_city(
            name=name, code=code, new_code=new_code
        )
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            services.create_city(city=city)
            data["message"] = "the city was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(data=data, status=status.HTTP_200_OK)


class StationAPI(APIView):
    def get(self, request):
        station = services.get_all_stations()
        serializer = serializers.StationSerializer(station, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        city_id = request.data.get("city")

        station, created = services.get_or_create_station(
            name=name, code=code, city_id=city_id
        )
        serializer = serializers.StationSerializer(station)
        data = {"data": serializer.data, "message": "was added succesfully"}

        if not created:
            data["message"] = "failed to add, the station already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_station(station=station)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}

        try:
            station = services.get_station_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        services.delete_station(station=station)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.data.get("code")
        name = request.data.get("name")
        new_code = request.data.get("new_code")
        city_id = request.data.get("city_id")
        station, created = services.update_or_create_station(
            name=name, code=code, new_code=new_code, city_id=city_id
        )
        serializer = serializers.StationSerializer(station)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            data["message"] = "the station was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)
        services.create_station(station=station)
        return Response(data=data, status=status.HTTP_200_OK)


class RouteAPI(APIView):
    def get(self, request):
        route = services.get_all_routes()
        serializer = serializers.RouteSerializer(route, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        station_list = request.data.get("stops")
        state = request.data.get("status")
        route, created = services.get_or_create_route(
            name=name, code=code, station_list=station_list, status=state
        )
        serializer = serializers.RouteSerializer(route)
        if created:
            services.create_route(route=route)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            route = services.get_route_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE ROUTE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_route(route=route)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        name = request.data.get("name")
        code = request.data.get("code")
        new_code = request.data.get("new_code")
        station_list = request.data.get("stops")
        state = request.data.get("status")
        route, created = services.update_or_create_route(
            name=name,
            code=code,
            station_list=station_list,
            status=state,
            new_code=new_code,
        )
        serializer = serializers.RouteSerializer(route)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            services.create_route(route=route)
            data["message"] = "the route was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=data, status=status.HTTP_200_OK)


class BusAPI(APIView):
    def get(self, request):
        buses = services.get_all_buses()
        serializer = serializers.BusSerializer(buses, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        state = request.data.get("status")
        code = request.data.get("code")
        bus, created = services.get_or_create_bus(status=state, code=code)
        serializer = serializers.BusSerializer(bus)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the bus already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_bus(bus=bus)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def put(self, request):
        code = request.data.get("code")
        state = request.data.get("status")
        new_code = request.data.get("new_code")
        bus, created = services.update_or_create_bus(
            status=state, code=code, new_code=new_code
        )
        serializer = serializers.BusSerializer(bus)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            services.create_bus(bus=bus)
            data["message"] = "the bus was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}

        try:
            bus = services.get_bus_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH BUS CODE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_bus(bus=bus)
        return Response(data=data, status=status.HTTP_200_OK)


class DriverAPI(APIView):
    def get(self, request):
        drivers = services.get_all_drivers()
        serializer = serializers.DriverSerializer(drivers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        state = request.data.get("status")
        rut = request.data.get("rut")
        name = request.data.get("name")
        driver, created = services.get_or_create_driver(
            status=state, name=name, rut=rut
        )
        serializer = serializers.DriverSerializer(driver)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the driver already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_driver(driver=driver)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def put(self, request):
        state = request.data.get("status")
        rut = request.data.get("rut")
        name = request.data.get("name")
        new_rut = request.data.get("new_rut")
        driver, created = services.update_or_create_driver(
            status=state, rut=rut, new_rut=new_rut, name=name
        )
        serializer = serializers.DriverSerializer(driver)
        data = {"data": serializer.data, "message": "Update Succesfully"}
        if created:
            services.create_driver(driver=driver)
            data["message"] = "the driver was added succesfully"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request):
        rut = request.data.get("rut")
        data = {"message": "Delete Succesfully"}

        try:
            driver = services.get_driver_by_rut(rut=rut)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH DRIVER RUT"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_driver(driver=driver)
        return Response(data=data, status=status.HTTP_200_OK)


class TravelAPI(APIView):
    def get(self, request):
        travels = services.get_all_travels()
        serializer = serializers.TravelSerializer(travels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        code = request.data.get("code")
        code_route = request.data.get("route")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        id_driver = request.data.get("driver")
        code_bus = request.data.get("bus")
        travel, created = services.get_or_create_travel(
            code=code,
            code_bus=code_bus,
            id_driver=id_driver,
            code_route=code_route,
            start_time=start_time,
            end_time=end_time,
        )
        serializer = serializers.TravelSerializer(travel)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the travel already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_travel(travel=travel)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def put(self, request):
        code = request.data.get("code")
        new_code = request.data.get("new_code")
        code_route = request.data.get("route")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        id_driver = request.data.get("driver")
        code_bus = request.data.get("bus")
        travel, created = services.update_or_create_travel(
            code=code,
            new_code=new_code,
            code_bus=code_bus,
            id_driver=id_driver,
            code_route=code_route,
            start_time=start_time,
            end_time=end_time,
        )
        serializer = serializers.TravelSerializer(travel)
        data = {"data": serializer.data, "message": "the travel was added succesfully"}
        if not created:
            data["message"] = "the travel was update succesfully"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_travel(travel=travel)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            travel = services.get_travel_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE TRAVEL"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_travel(travel=travel)
        return Response(data=data, status=status.HTTP_200_OK)


class PlaceAPI(APIView):
    def get(self, request):
        places = services.get_all_places()
        serializer = serializers.PlaceSerializer(places, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        code = request.data.get("code")
        available = request.data.get("available")
        code_travel = request.data.get("travel")
        place, created = services.get_or_create_place(
            code=code,
            available=available,
            code_travel=code_travel,
        )
        serializer = serializers.PlaceSerializer(place)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the place already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.data.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            place = services.get_place_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE PLACE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_place(place=place)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.data.get("code")
        new_code = request.data.get("new_code")
        available = request.data.get("available")
        code_travel = request.data.get("travel")
        place, created = services.update_or_create_place(
            code=code,
            available=available,
            new_code=new_code,
            code_travel=code_travel,
        )
        serializer = serializers.PlaceSerializer(place)
        data = {"data": serializer.data, "message": "the place was added succesfully"}
        if not created:
            data["message"] = "the place was update succesfully"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)
