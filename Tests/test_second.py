import requests
from config import SECOND_SITE
from src.baseclasses.response import Response
from src.schemas.user import User

# resp = requests.get(SECOND_SITE)
# print(resp.__getstate__())
# print(resp.url)


def test_getting_users_list():
    response = requests.get(SECOND_SITE)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)
