import json
import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


@pytest.mark.django_db
class TestDriver:
    url = reverse("driver_view")

    def create_data(self):
        baker.make(
            "travelManagement.Driver", name="Zeta", status="AVAILABLE", rut="18154231-5"
        )
        baker.make(
            "travelManagement.Driver", name="Juan", status="AVAILABLE", rut="18132231-6"
        )

    def test_get(self, api_client):
        self.create_data()
        expected = [
            {"name": "Zeta", "rut": "18154231-5", "status": "AVAILABLE"},
            {"name": "Juan", "rut": "18132231-6", "status": "AVAILABLE"},
        ]
        response = api_client.get(self.url, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post__driver_exist(self, api_client):
        self.create_data()
        param = {"name": "Zeta", "rut": "18154231-5", "status": "AVAILABLE"}

        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        expected_value = {
            "data": {"name": "Zeta", "rut": "18154231-5", "status": "AVAILABLE"},
            "message": "failed to add, the driver already exist",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_post__driver_no_exist(self, api_client):
        self.create_data()
        param = {"name": "Wates", "rut": "15.123.015-5", "status": "AVAILABLE"}

        response = api_client.post(
            self.url,
            param,
            format="json",
        )
        expected_value = {
            "data": {"name": "Wates", "rut": "15.123.015-5", "status": "AVAILABLE"},
            "message": "was added succesfully",
        }
        print("response post driver", response.content)
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED

    def test_put__driver_exist(self, api_client):
        self.create_data()
        param = {
            "name": "Zetacio",
            "rut": "18154231-5",
            "status": "AVAILABLE",
            "new_rut": "19154231-5",
        }

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"name": "Zetacio", "rut": "19154231-5", "status": "AVAILABLE"},
            "message": "Update Succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_put__driver_exist(self, api_client):
        param = {
            "name": "Zetacio",
            "rut": "18154231-5",
            "status": "AVAILABLE",
            "new_rut": "19154231-5",
        }

        response = api_client.put(self.url, param, format="json")
        expected_value = {
            "data": {"name": "Zetacio", "rut": "19154231-5", "status": "AVAILABLE"},
            "message": "the driver was added succesfully",
        }
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_driver_exist(self, api_client):
        self.create_data()
        param = {"rut": "18154231-5"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        expected_value = {"message": "Delete Succesfully"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_delete_driver_no_exist(self, api_client):
        param = {"rut": "18154231-5"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        expected_value = {"message": "NO MATCH DRIVER RUT"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_404_NOT_FOUND
