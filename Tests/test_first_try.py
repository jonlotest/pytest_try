import requests
from config import SITE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


# @pytest.mark.skip('[YD1] - Do not disturb')
def test_get_post():
    r = requests.get(url=SITE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)
