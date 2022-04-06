import json
from isort import code
import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework import status

# give access to db


@pytest.mark.django_db
class TestStation:
    # traslate the name of url
    url = reverse("station_view")

    def test_get(self, api_client):
        santiago = baker.make("travelManagement.City",
                              name="Santiago", code="SCL")
        chillan = baker.make("travelManagement.City",
                             name="Chillan", code="CHN")
        terminal_santiago = baker.make(
            "travelManagement.Station", name="San Borja", city=santiago)
        terminal_santiago2 = baker.make(
            "travelManagement.Station", name="Santiago", city=santiago)
        terminal_chillan = baker.make(
            "travelManagement.Station", name="Maria Teresa", city=chillan)
        terminal_chillan2 = baker.make(
            "travelManagement.Station", name="Maria Juana", city=chillan)
        expected = [
            {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
            {"name": "Santiago", "city": {"name": "Santiago", "code": "SCL"}},
            {"name": "Maria Teresa", "city": {"name": "Chillan", "code": "CHN"}},
            {"name": "Maria Juana", "city": {"name": "Chillan", "code": "CHN"}}
        ]
        response = api_client.get(self.url, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    def test_post_station_exist(self, api_client):
        santiago = baker.make("travelManagement.City",
                              name="Santiago", code="SCL")
        terminal_santiago = baker.make(
            "travelManagement.Station", name="San Borja", code="SNB", city=santiago)
        expected = {"data": {"name": "San Borja", "city": {"name": "Santiago",
                                                           "code": "SCL"}}, "message": "failed to add, the station already exist"}
        param = {"name": "San Borja", "code": "SNB",
                 "city": 1}

        response = api_client.post(self.url, param, format="json",)
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    # def test_post_station_not_exist(self, api_client):
    #     santiago = baker.make("travelManagement.City",
    #                           name="Santiago", code="SCL")
    #     expected = {"data": {"name": "San Borja", "city": {"name": "Santiago",
    #                                                        "code": "SCL"}}, "message": "was added succesfully"}
    #     param = {"name": "San Borja", "code": "SNB",
    #              "city": {"id": }}

    #     response = api_client.post(self.url, param, format="json",)
    #     print("response = ", response.content)
    #     print("expected = ", expected)
        # assert json.loads(response.content) == expected
        # assert response.status_code == status.HTTP_200_OK
