import json

import requests
from rest_framework import status


class ParentAPI:
    WS_URL = "http://127.0.0.1:8000/ws/"

    @classmethod
    def createWS(cls, data_json: str) -> str:
        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(cls.WS_URL, data=data_json, headers=headers)

            if response.status_code != status.HTTP_201_CREATED:
                raise Exception('STATUS CODE ERROR')

        except Exception as e:
            raise Exception('ERROR WHILE WEB SERVICE CALL', e.__str__())

        return json.loads(response.text)

