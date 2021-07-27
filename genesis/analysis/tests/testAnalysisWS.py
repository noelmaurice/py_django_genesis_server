"""
Testing variant data with database
"""
import json

import requests
from rest_framework import status

from genesis.analysis.tests.parentTest import ParentTest


class VariantWebServiceTestClass(ParentTest):
    """
    Class for testing the web services.
    """

    # server parameters
    HOST: str = 'localhost'
    PORT: int = 8000

    @classmethod
    def setUpTestData(cls):
        """
        Function called before all tests defined in the class
        """

    def setUp(self):
        """
        Function called before each test defined in the class
        """
        pass

    def test_insert_sample(self):
        """
        The web service for the sample insertion into the database is checked
        """
        data_json = '{"name": "splTOTO", "description": "Example of sample"}'

        data_dict = json.loads(data_json)

        request = 'http://{host}:{port}/ws/analysis/sample/'.format(
            host=VariantWebServiceTestClass.HOST,
            port=VariantWebServiceTestClass.PORT)

        response = requests.post(request, json=data_dict)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
