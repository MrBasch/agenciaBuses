from tkinter import N
from urllib import response
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from isort import code
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers, services
from .models import *

# Create your views here.


class FilterBuses(APIView):
    def get(self, request):
        route_code = request.GET.get("route_code")
        n = request.GET.get("N")
        data = services.selling_buses_by_route(route_code=route_code, N=n)
        return Response(data)


class AveriagePassenger(APIView):
    def get(self, request):
        route_code = request.GET.get("route_code")
        data = services.average_passangers_for_route(route_code=route_code)
        return Response(data)


class CreateData(APIView):
    def get(self, request):
        services.get_or_create_city(name="Santiago", code="STG")
        services.get_or_create_city(name="Achao", code="ACH")
        services.get_or_create_city(name="Algarrobo", code="ALG")
        services.get_or_create_city(name="Buin", code="BUI")
        services.get_or_create_city(name="Chillan", code="YAI")
        services.get_or_create_city(name="Coyhaique", code="CXQ")

        services.get_or_create_station(name="San Borja", code="SNBJA", city_id=1)
        services.get_or_create_station(name="Alameda", code="ALMD", city_id=1)
        services.get_or_create_station(name="Terminal Sur", code="TSUR", city_id=1)
        services.get_or_create_station(
            name="Terminal Alto Jahuel", code="TAHL", city_id=4
        )
        services.get_or_create_station(name="Estacion Buin", code="EBN", city_id=4)
        services.get_or_create_station(
            name="Terminal del Centro", code="TCEN", city_id=5
        )
        services.get_or_create_station(
            name="Terminal Maria Teresa", code="TMT", city_id=5
        )
        services.get_or_create_station(name="Terminal Algarrobo", code="TAL", city_id=3)
        services.get_or_create_station(
            name="Terminal Aguilas Patagonicas", code="TAP", city_id=6
        )
        services.get_or_create_station(
            name="Terminal Municipal Coyhaique", code="TMC", city_id=6
        )

        services.get_or_create_route(
            name="Santiago-Chillán",
            code="STG-YAI",
            station_list=[1, 2, 6],
            status="AVAILABLE",
        )
        services.get_or_create_route(
            name="Santiago-Buin",
            code="STG-BUI",
            station_list=[1, 4],
            status="AVAILABLE",
        )
        services.get_or_create_route(
            name="Buin-Algarrobo",
            code="BUI-ALG",
            station_list=[5, 8],
            status="AVAILABLE",
        )

        services.get_or_create_bus(code="Bus1", status="AVAILABLE")
        services.get_or_create_bus(code="Bus2", status="AVAILABLE")
        services.get_or_create_bus(code="Bus3", status="AVAILABLE")
        services.get_or_create_bus(code="Bus4", status="AVAILABLE")

        services.get_or_create_driver(
            name="Zayaco", rut="19.123.456-8", status="AVAILABLE"
        )
        services.get_or_create_driver(
            name="Gates", rut="19.123.432-1", status="AVAILABLE"
        )
        services.get_or_create_driver(
            name="Bigote", rut="19.223.432-5", status="AVAILABLE"
        )
        services.get_or_create_driver(
            name="Juancho", rut="12.123.432-1", status="AVAILABLE"
        )

        services.get_or_create_travel(
            code="T1",
            code_route="STG-YAI",
            code_bus="Bus1",
            id_driver=1,
            start_time="2022-02-04T10:30:00Z",
            end_time="2022-02-04T18:30:00Z",
        )
        services.get_or_create_travel(
            code="T2",
            code_route="STG-BUI",
            code_bus="Bus2",
            id_driver=2,
            start_time="2022-02-04T10:30:00Z",
            end_time="2022-03-04T18:30:00Z",
        )
        services.get_or_create_travel(
            code="T3",
            code_route="BUI-ALG",
            code_bus="Bus3",
            id_driver=3,
            start_time="2022-04-04T10:30:00Z",
            end_time="2022-05-04T18:30:00Z",
        )
        services.get_or_create_travel(
            code="T4",
            code_route="BUI-ALG",
            code_bus="Bus2",
            id_driver=2,
            start_time="2022-04-04T10:30:00Z",
            end_time="2022-05-04T18:30:00Z",
        )

        services.get_or_create_place(code_travel="T1", code="A1", available=True)
        services.get_or_create_place(code_travel="T1", code="A2", available=False)
        services.get_or_create_place(code_travel="T1", code="A3", available=False)
        services.get_or_create_place(code_travel="T1", code="A4", available=False)
        services.get_or_create_place(code_travel="T1", code="A5", available=False)
        services.get_or_create_place(code_travel="T1", code="A6", available=False)
        services.get_or_create_place(code_travel="T1", code="A7", available=False)
        services.get_or_create_place(code_travel="T1", code="A8", available=False)
        services.get_or_create_place(code_travel="T1", code="A9", available=True)
        services.get_or_create_place(code_travel="T1", code="A10", available=True)

        services.get_or_create_place(code_travel="T2", code="B1", available=False)
        services.get_or_create_place(code_travel="T2", code="B2", available=False)
        services.get_or_create_place(code_travel="T2", code="B3", available=False)
        services.get_or_create_place(code_travel="T2", code="B4", available=False)
        services.get_or_create_place(code_travel="T2", code="B5", available=False)
        services.get_or_create_place(code_travel="T2", code="B6", available=False)
        services.get_or_create_place(code_travel="T2", code="B7", available=True)
        services.get_or_create_place(code_travel="T2", code="B8", available=True)
        services.get_or_create_place(code_travel="T2", code="B9", available=True)
        services.get_or_create_place(code_travel="T2", code="B10", available=True)

        services.get_or_create_place(code_travel="T3", code="C1", available=True)
        services.get_or_create_place(code_travel="T3", code="C3", available=True)
        services.get_or_create_place(code_travel="T3", code="C3", available=True)
        services.get_or_create_place(code_travel="T3", code="C4", available=True)
        services.get_or_create_place(code_travel="T3", code="C5", available=False)
        services.get_or_create_place(code_travel="T3", code="C6", available=False)
        services.get_or_create_place(code_travel="T3", code="C7", available=False)
        services.get_or_create_place(code_travel="T3", code="C8", available=False)
        services.get_or_create_place(code_travel="T3", code="C9", available=False)
        services.get_or_create_place(code_travel="T3", code="C10", available=False)

        services.get_or_create_place(code_travel="T4", code="D1", available=True)
        services.get_or_create_place(code_travel="T4", code="D3", available=False)
        services.get_or_create_place(code_travel="T4", code="D3", available=True)
        services.get_or_create_place(code_travel="T4", code="D4", available=False)
        services.get_or_create_place(code_travel="T4", code="D5", available=False)
        services.get_or_create_place(code_travel="T4", code="D6", available=False)
        services.get_or_create_place(code_travel="T4", code="D7", available=False)
        services.get_or_create_place(code_travel="T4", code="D8", available=False)
        services.get_or_create_place(code_travel="T4", code="D9", available=False)
        services.get_or_create_place(code_travel="T4", code="D10", available=False)

        services.get_or_create_passenger(
            place_code="A2", name="Juan", rut="13.145.587-1"
        )
        services.get_or_create_passenger(
            place_code="A3", name="Ricardo", rut="12.445.587-1"
        )
        services.get_or_create_passenger(
            place_code="A4", name="Maria", rut="12.845.587-1"
        )
        services.get_or_create_passenger(
            place_code="A5", name="Nicolas", rut="12.545.587-1"
        )
        services.get_or_create_passenger(
            place_code="A6", name="Haku", rut="12.175.587-1"
        )
        services.get_or_create_passenger(
            place_code="A7", name="Milton", rut="12.455.587-1"
        )
        services.get_or_create_passenger(
            place_code="A8", name="Yahaira", rut="12.245.587-1"
        )

        services.get_or_create_passenger(
            place_code="B1", name="Pancrasio", rut="13.145.587-1"
        )
        services.get_or_create_passenger(
            place_code="B2", name="Jonathan", rut="14.145.587-8"
        )
        services.get_or_create_passenger(
            place_code="B3", name="Jhon", rut="12.145.880-1"
        )
        services.get_or_create_passenger(
            place_code="B4", name="Lemon", rut="12.145.557-3"
        )
        services.get_or_create_passenger(
            place_code="B5", name="Zoro", rut="12.145.407-1"
        )
        services.get_or_create_passenger(
            place_code="B6", name="Morgan", rut="12.145.587-5"
        )
        services.get_or_create_passenger(
            place_code="B10", name="Soren", rut="12.872.587-1"
        )
        return Response("Data created")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CityAPI(APIView):
    def get(self, request):
        cities = services.get_all_cities()
        serializer = serializers.CitySerializer(cities, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.GET.get("name")
        code = request.GET.get("code")
        city, created = services.get_or_create_city(name=name, code=code)
        serializer = serializers.CitySerializer(city)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the city already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.GET.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            city = services.get_city_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_city(city=city)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.GET.get("code")
        name = request.GET.get("name")
        new_code = request.GET.get("new_code")
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
        name = request.GET.get("name")
        code = request.GET.get("code")
        city_id = request.GET.get("city")

        station, created = services.get_or_create_station(
            name=name, code=code, city_id=city_id
        )
        serializer = serializers.StationSerializer(station)
        data = {"data": serializer.data, "message": "was added succesfully"}

        if not created:
            data["message"] = "failed to add, the station already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        code = request.GET.get("code")
        data = {"message": "Delete Succesfully"}

        try:
            station = services.get_station_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE CITY"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        services.delete_station(station=station)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.GET.get("code")
        name = request.GET.get("name")
        new_code = request.GET.get("new_code")
        city_id = request.GET.get("city_id")
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
        name = request.GET.get("name")
        code = request.GET.get("code")
        station_list = request.GET.get("stops")
        state = request.GET.get("status")
        route, created = services.get_or_create_route(
            name=name, code=code, station_list=station_list, status=state
        )
        serializer = serializers.RouteSerializer(route)
        if created:
            services.create_route(route=route)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        code = request.GET.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            route = services.get_route_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE ROUTE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_route(route=route)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        name = request.GET.get("name")
        code = request.GET.get("code")
        new_code = request.GET.get("new_code")
        station_list = request.GET.get("stops")
        state = request.GET.get("status")
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
        state = request.GET.get("status")
        code = request.GET.get("code")
        bus, created = services.get_or_create_bus(status=state, code=code)
        serializer = serializers.BusSerializer(bus)
        data = {"data": serializer.data, "message": "was added succesfully"}
        if not created:
            data["message"] = "failed to add, the bus already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        services.create_bus(bus=bus)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def put(self, request):
        code = request.GET.get("code")
        state = request.GET.get("status")
        new_code = request.GET.get("new_code")
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
        code = request.GET.get("code")
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
        state = request.GET.get("status")
        rut = request.GET.get("rut")
        name = request.GET.get("name")
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
        state = request.GET.get("status")
        rut = request.GET.get("rut")
        name = request.GET.get("name")
        new_rut = request.GET.get("new_rut")
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
        rut = request.GET.get("rut")
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
        code = request.GET.get("code")
        code_route = request.GET.get("route")
        start_time = request.GET.get("start_time")
        end_time = request.GET.get("end_time")
        id_driver = request.GET.get("driver")
        code_bus = request.GET.get("bus")
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
        code = request.GET.get("code")
        new_code = request.GET.get("new_code")
        code_route = request.GET.get("route")
        start_time = request.GET.get("start_time")
        end_time = request.GET.get("end_time")
        id_driver = request.GET.get("driver")
        code_bus = request.GET.get("bus")
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
        code = request.GET.get("code")
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
        code = request.GET.get("code")
        available = request.GET.get("available")
        code_travel = request.GET.get("travel")
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
        code = request.GET.get("code")
        data = {"message": "Delete Succesfully"}
        try:
            place = services.get_place_by_code(code=code)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH CODE PLACE"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_place(place=place)
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request):
        code = request.GET.get("code")
        new_code = request.GET.get("new_code")
        available = request.GET.get("available")
        code_travel = request.GET.get("travel")
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


class PassengerAPI(APIView):
    def get(self, request):
        passengers = services.get_all_passenger()
        serializer = serializers.PassengerSerializer(passengers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        place_code = request.GET.get("place")
        name = request.GET.get("name")
        rut = request.GET.get("rut")
        new_rut = request.GET.get("new_rut")
        passenger, created = services.update_or_create_passenger(
            place_code=place_code,
            name=name,
            rut=rut,
            new_rut=new_rut,
        )
        serializer = serializers.PassengerSerializer(passenger)
        data = {"data": serializer.data, "message": "the place was added succesfully"}
        if not created:
            data["message"] = "the place was update succesfully"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def post(self, request):
        place_code = request.GET.get("place")
        name = request.GET.get("name")
        rut = request.GET.get("rut")

        passenger, created = services.get_or_create_passenger(
            place_code=place_code,
            name=name,
            rut=rut,
        )
        serializer = serializers.PassengerSerializer(passenger)
        data = {"data": serializer.data, "message": "was added succesfully"}

        if not created:
            data["message"] = "failed to add, the passenger already exist"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        id = request.GET.get("id")
        data = {"message": "Delete Succesfully"}

        try:
            passenger = services.get_passenger_by_id(id=id)
        except ObjectDoesNotExist:
            data["message"] = "NO MATCH ID PASSENGER"
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        services.delete_passanger(passenger=passenger)
        return Response(data=data, status=status.HTTP_200_OK)
