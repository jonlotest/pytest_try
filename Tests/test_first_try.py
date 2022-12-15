import requests
from config import SITE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA


def test_get_post():
    r = requests.get(url=SITE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)
