import json
from email.policy import default

import pytest
from django.urls import reverse
from isort import code
from model_bakery import baker
from rest_framework import status

# give access to db


@pytest.mark.django_db
class TestStation:
    # traslate the name of url
    url = reverse("station_view")

    def create_data(self):
        santiago = baker.make("travelManagement.City", name="Santiago", code="SCL")
        chillan = baker.make("travelManagement.City", name="Chillan", code="CHN")
        terminal_santiago = baker.make(
            "travelManagement.Station", name="San Borja", city=santiago, code="SNB"
        )
        terminal_santiago2 = baker.make(
            "travelManagement.Station", name="Santiago", city=santiago, code="STG"
        )
        terminal_chillan = baker.make(
            "travelManagement.Station", name="Maria Teresa", city=chillan, code="TMT"
        )
        terminal_chillan2 = baker.make(
            "travelManagement.Station", name="Maria Juana", city=chillan, code="TMJ"
        )

    def test_get(self, api_client):
        self.create_data()
        expected = [
            {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
            {"name": "Santiago", "city": {"name": "Santiago", "code": "SCL"}},
            {"name": "Maria Teresa", "city": {"name": "Chillan", "code": "CHN"}},
            {"name": "Maria Juana", "city": {"name": "Chillan", "code": "CHN"}},
        ]
        response = api_client.get(self.url, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post_station_exist(self, api_client):
        self.create_data()

        # exist "data": {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},

        param = {"name": "San Borja", "code": "SNB", "city": 1}
        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        expected = {
            "data": {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
            "message": "failed to add, the station already exist",
        }
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post_station_not_exist(self, api_client):
        # DB {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}
        self.create_data()
        param = {"name": "Estacion Central", "code": "ENC", "city": 1}
        expected = {
            "data": {
                "name": "Estacion Central",
                "city": {"name": "Santiago", "code": "SCL"},
            },
            "message": "was added succesfully",
        }

        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_station_exist(self, api_client):
        self.create_data()
        param = {"code": "SNB"}
        expected_value = {"message": "Delete Succesfully"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_delete_station_not_exist(self, api_client):
        param = {"code": "JM#"}
        expected_value = {"message": "NO MATCH CODE CITY"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_put__station_exist(self, api_client):
        self.create_data()
        param = {"code": "SNB", "name": "Chile", "new_code": "CHI", "city_id": 1}

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"name": "Chile", "city": {"name": "Santiago", "code": "SCL"}},
            "message": "Update Succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_put__station_not_exist(self, api_client):
        self.create_data()
        param = {"code": "SJN", "name": "Alameda", "new_code": "ALM", "city_id": 1}

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"name": "Alameda", "city": {"name": "Santiago", "code": "SCL"}},
            "message": "the station was added succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED
