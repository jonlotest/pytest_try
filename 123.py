import requests
from config import SITE_URL

resp = requests.get(SITE_URL)
print(resp.json())


