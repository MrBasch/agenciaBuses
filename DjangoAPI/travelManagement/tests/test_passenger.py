import json

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


@pytest.mark.django_db(transaction=True)
class TestPlace:
    url = reverse("passenger_view")

    def setup_method(self):
        self.permissions = Permission.objects.all()

        self.group = baker.make("auth.Group", name="grupo-usuarios")
        self.group.permissions.add(*self.permissions)
        self.user = baker.make(get_user_model(), username="test")
        self.user.set_password("123456A-")
        self.user.groups.add(self.group)
        self.user.save()

        self.santiago = baker.make("travelManagement.City", name="Santiago", code="SCL")
        self.chillan = baker.make("travelManagement.City", name="Chillan", code="CHN")
        self.terminal_santiago = baker.make(
            "travelManagement.Station", name="San Borja", city=self.santiago
        )
        self.terminal_santiago2 = baker.make(
            "travelManagement.Station", name="Santiago", city=self.santiago
        )
        self.terminal_chillan = baker.make(
            "travelManagement.Station", name="Maria Teresa", city=self.chillan
        )
        self.terminal_chillan2 = baker.make(
            "travelManagement.Station", name="Maria Juana", city=self.chillan
        )

        self.route_santiago_chillan = baker.make(
            "travelManagement.Route",
            code="XR1",
            stops=[
                self.terminal_santiago,
                self.terminal_santiago2,
                self.terminal_chillan2,
            ],
            name="Santiago - Chillan",
            status="AVAILABLE",
        )
        self.route_chillan_santiago = baker.make(
            "travelManagement.Route",
            code="XR3",
            stops=[
                self.terminal_chillan,
                self.terminal_chillan2,
                self.terminal_santiago,
            ],
            name="Chillan - Santiago",
            status="AVAILABLE",
        )
        self.zeta_driver = baker.make(
            "travelManagement.Driver", name="Zeta", status="AVAILABLE", rut="18154231-5"
        )
        self.juan_driver = baker.make(
            "travelManagement.Driver", name="Juan", status="AVAILABLE", rut="18132231-6"
        )
        self.bus_1 = baker.make("travelManagement.Bus", status="AVAILABLE", code="JPK")
        self.bus_2 = baker.make("travelManagement.Bus", status="AVAILABLE", code="JVV")
        self.travel_1 = baker.make(
            "travelManagement.Travel",
            code="TFRS",
            route=self.route_santiago_chillan,
            bus=self.bus_1,
            driver=self.juan_driver,
            start_time="2022-02-04 11:30:45",
            end_time="2022-02-04 18:30:00",
        )
        self.travel_2 = baker.make(
            "travelManagement.Travel",
            code="TSFF",
            route=self.route_chillan_santiago,
            bus=self.bus_2,
            driver=self.zeta_driver,
            start_time="2022-02-05 18:30:00",
            end_time="2022-02-05 23:30:00",
        )
        self.place_1 = baker.make(
            "travelManagement.Place", travel=self.travel_1, code="G1V", available=True
        )
        self.place_2 = baker.make(
            "travelManagement.Place", travel=self.travel_1, code="G1P", available=True
        )
        self.place_3 = baker.make(
            "travelManagement.Place", travel=self.travel_1, code="G2V", available=True
        )
        self.place_4 = baker.make(
            "travelManagement.Place", travel=self.travel_1, code="G2P", available=True
        )
        self.passenger_1 = baker.make(
            "travelManagement.Passenger",
            place=self.place_1,
            name="Guaripolo",
            rut="12.123.123-5",
        )
        self.passenger_2 = baker.make(
            "travelManagement.Passenger",
            place=self.place_2,
            name="Wachimingo",
            rut="21.243.123-5",
        )

    def test_get(self, api_client):
        api_client.force_authenticate(self.user)
        response = api_client.get(
            self.url,
            format="json",
        )
        expected = [
            {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1V",
                    "available": True,
                },
                "name": "Guaripolo",
                "rut": "12.123.123-5",
            },
            {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1P",
                    "available": True,
                },
                "name": "Wachimingo",
                "rut": "21.243.123-5",
            },
        ]
        breakpoint()
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_delete_passenger_exist(self, api_client):
        param = {"id": self.passenger_1.id}
        response = api_client.delete(self.url, param, format="json")
        expected = {"message": "Delete Succesfully"}
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_delete_passenger_no_exist(self, api_client):
        param = {"id": 5}
        response = api_client.delete(self.url, param, format="json")
        expected = {"message": "NO MATCH ID PASSENGER"}
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_post_passenger_exist(self, api_client):
        param = {
            "place": self.place_1.code,
            "name": self.passenger_1.name,
            "rut": self.passenger_1.rut,
        }
        expected = {
            "data": {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1V",
                    "available": True,
                },
                "name": "Guaripolo",
                "rut": "12.123.123-5",
            },
            "message": "failed to add, the passenger already exist",
        }
        response = api_client.post(self.url, param, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post_passenger_no_exist(self, api_client):
        param = {
            "place": self.place_1.code,
            "name": "jose jose",
            "rut": "18.123.456-5",
        }
        expected = {
            "data": {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1V",
                    "available": True,
                },
                "name": "jose jose",
                "rut": "18.123.456-5",
            },
            "message": "was added succesfully",
        }
        response = api_client.post(self.url, param, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_201_CREATED

    def test_put_passanger_exist(self, api_client):
        param = {
            "place": self.place_1.code,
            "name": "el bigote",
            "rut": self.passenger_1.rut,
            "new_rut": "15.154.235-5",
        }
        expected = {
            "data": {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1V",
                    "available": True,
                },
                "name": "Guaripolo",
                "rut": "12.123.123-5",
            },
            "message": "the place was update succesfully",
        }
        response = api_client.put(self.url, param, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_put_passanger_no_exist(self, api_client):
        param = {
            "place": self.place_1.code,
            "name": "el bigote",
            "rut": "12.341.123-6",
            "new_rut": "15.154.235-5",
        }
        expected = {
            "data": {
                "place": {
                    "travel": {
                        "code": "TFRS",
                        "route": {
                            "code": "XR1",
                            "stops": [
                                {
                                    "name": "San Borja",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Santiago",
                                    "city": {"name": "Santiago", "code": "SCL"},
                                },
                                {
                                    "name": "Maria Juana",
                                    "city": {"name": "Chillan", "code": "CHN"},
                                },
                            ],
                            "name": "Santiago - Chillan",
                            "status": "AVAILABLE",
                        },
                        "bus": {"code": "JPK", "status": "AVAILABLE"},
                        "driver": {
                            "name": "Juan",
                            "rut": "18132231-6",
                            "status": "AVAILABLE",
                        },
                        "start_time": "2022-02-04T11:30:45Z",
                        "end_time": "2022-02-04T18:30:00Z",
                    },
                    "code": "G1V",
                    "available": True,
                },
                "name": "el bigote",
                "rut": "15.154.235-5",
            },
            "message": "the place was added succesfully",
        }
        response = api_client.put(self.url, param, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_201_CREATED
