import json
import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
class TestCities:
    # traslate the name of url
    url = reverse("bus_view")

    def create_data(self):
        baker.make("travelManagement.Bus", status="AVAILABLE", code="JPK")
        baker.make("travelManagement.Bus", status="AVAILABLE", code="JVV")

    def test_get(self, api_client):
        self.create_data()
        expected = [
            {"code": "JPK", "status": "AVAILABLE"},
            {"code": "JVV", "status": "AVAILABLE"},
        ]
        response = api_client.get(
            self.url,
            headers={"Authorization": "Token 766c1cfc137888181d2c6f8b0e14a7dd2dc1f8ea"},
            format="json",
        )
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post__bus_exist(self, api_client):
        self.create_data()
        param = {"status": "AVAILABLE", "code": "JPK"}

        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        expected_value = {
            "data": {"code": "JPK", "status": "AVAILABLE"},
            "message": "failed to add, the bus already exist",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_post__bus_not_exist(self, api_client):
        self.create_data()
        param = {"status": "AVAILABLE", "code": "JJJ"}

        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        expected_value = {
            "data": {"code": "JJJ", "status": "AVAILABLE"},
            "message": "was added succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED

    def test_put__bus_exist(self, api_client):
        self.create_data()
        param = {"code": "JVV", "status": "AVAILABLE", "new_code": "P3P"}

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"code": "P3P", "status": "AVAILABLE"},
            "message": "Update Succesfully",
        }

        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_put__bus_exist(self, api_client):
        self.create_data()
        param = {"code": "P3P", "status": "AVAILABLE", "new_code": "P3P"}

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"code": "P3P", "status": "AVAILABLE"},
            "message": "the bus was added succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_bus_exist(self, api_client):
        self.create_data()
        param = {"code": "JVV"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        expected_value = {"message": "Delete Succesfully"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_delete_bus_not_exist(self, api_client):
        self.create_data()
        param = {"code": "QQQ"}
        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        expected_value = {"message": "NO MATCH BUS CODE"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_404_NOT_FOUND
