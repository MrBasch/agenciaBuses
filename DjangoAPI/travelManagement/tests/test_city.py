import json
import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status

# give access to db


@pytest.mark.django_db
class TestCities:
    # traslate the name of url
    url = reverse("cities_view")

    def test_get(self, api_client):
        santiago = baker.make("travelManagement.City",
                              name="Santiago", code="SCL")
        chillan = baker.make("travelManagement.City",
                             name="Chillan", code="CHN")
        expected_cities = [
            {"name": santiago.name, "code": santiago.code},
            {"name": chillan.name, "code": chillan.code},
        ]
        response = api_client.get(self.url, format="json")

        assert json.loads(response.content) == expected_cities
        assert response.status_code == status.HTTP_200_OK

    def test_post__city_exist(self, api_client):
        city = baker.make("travelManagement.City", name="Santiago", code="SCL")
        param = {"name": "Santiago", "code": "SCL"}

        response = api_client.post(self.url, param, format="json",)
        expected_value = {"data": param,
                          "message": "failed to add, the city already exist"}

        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_post__city_no_exist(self, api_client):
        city = {"name": "Viña del mar", "code": "VDM"}

        response = api_client.post(self.url, city, format="json",)
        expected_value = {"data": city,
                          "message": "was added succesfully"}

        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_city_exist(self, api_client):
        city = baker.make("travelManagement.City", name="Santiago", code="SCL")
        param = {"code": "SCL"}

        response = api_client.delete(self.url, param, format="json",)
        expected_value = {"message": "Delete Succesfully"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_delete_city_no_exist(self, api_client):
        param = {"code": "SCL"}

        response = api_client.delete(self.url, param, format="json",)
        expected_value = {"message": "NO MATCH CODE CITY"}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_put__city_exist(self, api_client):
        city = baker.make("travelManagement.City", name="Santiago", code="SCL")
        param = {"code":  "SCL", "name": "PEPE", "new_code": "P3P"}

        response = api_client.put(self.url, param, format="json")
        expected_value = {'data': {'name': 'PEPE',
                                   'code': 'P3P'}, 'message': 'Update Succesfully'}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_put__city_not_exist(self, api_client):
        param = {"code":  "P3PA", "name": "PEPA", "new_code": "P3P5"}

        response = api_client.put(self.url, param, format="json")
        expected_value = {'data': {'name': 'PEPA',
                                   'code': 'P3P5'}, 'message': 'the city was added succesfully'}
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_201_CREATED
