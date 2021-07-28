import json

import requests
from django.test import TestCase
from requests import Response
from rest_framework import status, request


class ParentTest(TestCase):
    """
    All the test objects managed by django test inherit of ParentTest
    """

    # server parameters
    HOST: str = 'localhost'
    PORT: int = 8000

    @staticmethod
    def postWS(url: str, data_json: str) -> Response:
        """
        The post web service
        :param url: web service url
        :param data_json: data to recorded
        :return: response object in accordance with the request
        """
        data_dict = json.loads(data_json)

        request = url.format(
                    host = ParentTest.HOST,
                    port = ParentTest.PORT)

        return requests.post(request, json=data_dict)