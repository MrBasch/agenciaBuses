import pytest
from rest_framework.test import APIClient

# instance of client


@pytest.fixture
def api_client():
    return APIClient()
