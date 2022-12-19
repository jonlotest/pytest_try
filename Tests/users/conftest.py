import pytest
import requests
from config import SECOND_SITE


@pytest.fixture()
def get_users():
    response = requests.get(SECOND_SITE)
    return response
