import pytest
import requests
from config import SECOND_SITE, YA_PRAKTIKUM, URL_API_YA


@pytest.fixture()
def get_users():
    response = requests.get(SECOND_SITE)
    return response


def test_get_response():
    response = requests.get(YA_PRAKTIKUM)
    print(response.content)
