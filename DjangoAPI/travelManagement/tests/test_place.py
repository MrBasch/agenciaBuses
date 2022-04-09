import json

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
class TestPlace:
    url = reverse("place_view")

    def setup_method(self):
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

    def test_get(self, api_client):
        response = api_client.get(self.url, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_delete_place_exist(self, api_client):
        param = {"code": "G1V"}
        response = api_client.delete(self.url, param, format="json")
        expected = {"message": "Delete Succesfully"}
        print("response SSSS= ", response.content)
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_delete_place_not_exist(self, api_client):
        param = {"code": "A1V"}
        response = api_client.delete(self.url, param, format="json")
        expected = {"message": "NO MATCH CODE PLACE"}
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_post_place_exist(self, api_client):
        param = {"code": "G1V", "available": True, "travel": self.travel_2.code}
        expected = {
            "data": {
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
            "message": "failed to add, the place already exist",
        }
        response = api_client.post(self.url, param, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post_place_no_exist(self, api_client):
        param = {"code": "GGTST", "available": True, "travel": self.travel_2.code}
        response = api_client.post(self.url, param, format="json")
        expected = {
            "data": {
                "travel": {
                    "code": "TSFF",
                    "route": {
                        "code": "XR3",
                        "stops": [
                            {
                                "name": "San Borja",
                                "city": {"name": "Santiago", "code": "SCL"},
                            },
                            {
                                "name": "Maria Teresa",
                                "city": {"name": "Chillan", "code": "CHN"},
                            },
                            {
                                "name": "Maria Juana",
                                "city": {"name": "Chillan", "code": "CHN"},
                            },
                        ],
                        "name": "Chillan - Santiago",
                        "status": "AVAILABLE",
                    },
                    "bus": {"code": "JVV", "status": "AVAILABLE"},
                    "driver": {
                        "name": "Zeta",
                        "rut": "18154231-5",
                        "status": "AVAILABLE",
                    },
                    "start_time": "2022-02-05T18:30:00Z",
                    "end_time": "2022-02-05T23:30:00Z",
                },
                "code": "GGTST",
                "available": True,
            },
            "message": "was added succesfully",
        }
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_201_CREATED

    def test_put_place_exist(self, api_client):
        param = {
            "code": "G1V",
            "new_code": "SAS",
            "available": True,
            "travel": self.travel_2.code,
        }
        expected = {
            "data": {
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
            "message": "the place was update succesfully",
        }
        response = api_client.put(self.url, param, format="json")
        print("response = ", response.content)
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK
