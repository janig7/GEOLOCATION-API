import requests
import os
import dotenv

from core.settings import BASE_DIR

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

API_KEY = os.environ['API_KEY']
PAYLOAD = {'access_key': API_KEY}


class IPStack:
    def __init__(self, ip=None, url=None):
        """
        Constructor

        """
        self._ip = ip
        self._url = url
        self._country = None
        self._geo_data = None
        self._raw_data = None

    def _connect(self):
        url = ''
        if self._url is not None:
            url = f'http://api.ipstack.com/{self._url}'
        if self._ip is not None:
            url = f'http://api.ipstack.com/{self._ip}'
        res = requests.get(url, params=PAYLOAD)
        if res.ok:
            self._raw_data = res.json()

    def _parse(self):
        self._connect()
        self._location = {
            'country': self._raw_data.get('country_name'),
            'city': self._raw_data.get('city'),
        }

        self._geo_data = {
            'latitude': self._raw_data.get('latitude'),
            'longitude': self._raw_data.get('longitude'),
        }

    def get_data(self):
        self._parse()

        return {
            'country': self._location['country'],
            'city': self._location['city'],
            'latitude': self._geo_data['latitude'],
            'longitude': self._geo_data['longitude'],
        }
