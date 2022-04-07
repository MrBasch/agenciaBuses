import json
from email.policy import default

import pytest
from django.urls import reverse
from isort import code
from model_bakery import baker
from rest_framework import status

# give access to db


@pytest.mark.django_db
class TestRoute:
    url = reverse("route_view")

    def create_data(self):
        santiago = baker.make("travelManagement.City", name="Santiago", code="SCL")
        chillan = baker.make("travelManagement.City", name="Chillan", code="CHN")
        terminal_santiago = baker.make(
            "travelManagement.Station", name="San Borja", city=santiago
        )
        terminal_santiago2 = baker.make(
            "travelManagement.Station", name="Santiago", city=santiago
        )
        terminal_chillan = baker.make(
            "travelManagement.Station", name="Maria Teresa", city=chillan
        )
        terminal_chillan2 = baker.make(
            "travelManagement.Station", name="Maria Juana", city=chillan
        )

        route_santiago_chillan = baker.make(
            "travelManagement.Route",
            code="XR1",
            stops=[terminal_santiago, terminal_santiago2, terminal_chillan2],
            name="Santiago - Chillan",
            status="AVAILABLE",
        )
        route_chillan_santiago = baker.make(
            "travelManagement.Route",
            code="XR3",
            stops=[terminal_chillan, terminal_chillan2, terminal_santiago],
            name="Chillan - Santiago",
            status="AVAILABLE",
        )
        stops = [terminal_santiago, terminal_santiago2, terminal_chillan2]
        print("stops =", stops)

    def test_get(self, api_client):
        self.create_data()
        expected = [
            {
                "code": "XR1",
                "stops": [
                    {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
                    {"name": "Santiago", "city": {"name": "Santiago", "code": "SCL"}},
                    {"name": "Maria Juana", "city": {"name": "Chillan", "code": "CHN"}},
                ],
                "name": "Santiago - Chillan",
                "status": "AVAILABLE",
            },
            {
                "code": "XR3",
                "stops": [
                    {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
                    {
                        "name": "Maria Teresa",
                        "city": {"name": "Chillan", "code": "CHN"},
                    },
                    {"name": "Maria Juana", "city": {"name": "Chillan", "code": "CHN"}},
                ],
                "name": "Chillan - Santiago",
                "status": "AVAILABLE",
            },
        ]
        response = api_client.get(self.url, format="json")
        assert json.loads(response.content) == expected
        assert response.status_code == status.HTTP_200_OK

    # def test_post_route_exist(self, api_client):
    #     self.create_data()
    #     expected = [
    #         {
    #             "code": "XR1",
    #             "stops": [
    #                 {"name": "San Borja", "city": {"name": "Santiago", "code": "SCL"}},
    #                 {"name": "Santiago", "city": {"name": "Santiago", "code": "SCL"}},
    #                 {"name": "Maria Juana", "city": {"name": "Chillan", "code": "CHN"}},
    #             ],
    #             "name": "Santiago Chillan",
    #             "status": "AVAILABLE",
    #         }
    #     ]
    #     param = {
    #         "code": "XR1",
    #         "stops": [1, 2, 4],
    #         "name": "Santiago Chillan",
    #         "status": "AVAILABLE",
    #     }

    #     response = api_client.post(
    #         self.url,
    #         param,
    #         format="json",
    #     )
    #     print("response = ", response.content)
    # assert json.loads(response.content) == expected
    # assert response.status_code == status.HTTP_200_OK
    def test_delete_route_exist(self, api_client):
        self.create_data()
        param = {"code": "XR1"}
        expected_value = {"message": "Delete Succesfully"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_200_OK

    def test_delete_route_no_exist(self, api_client):
        param = {"code": "JM#"}
        expected_value = {"message": "NO MATCH CODE ROUTE"}

        response = api_client.delete(
            self.url,
            param,
            format="json",
        )
        assert json.loads(response.content) == expected_value
        assert response.status_code == status.HTTP_404_NOT_FOUND
