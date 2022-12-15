import requests
from config import SITE_URL


def test_get_post():
    response = requests.get(url=SITE_URL)
    print(response.json())

