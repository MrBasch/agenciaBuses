from asyncio.windows_events import NULL
from telnetlib import STATUS
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from . import serializers
from .services import get_all_cities, get_or_create_city

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
