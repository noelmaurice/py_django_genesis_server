"""
Testing variant data with database
"""
import json

import requests

from variant.model_data.repository.parentRepository import ComparatorEnum
from variant.tests.parentTest import ParentTest


class VariantWebServiceTestClass(ParentTest):
    """
    Class for testing the web services.

    For each test, only the request status of the web service is tested because the repository used is tested
    by the data model_data tests.
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


    def test_insert_variant(self):
        """
        The web service for the variant insertion into the database is checked
        """
        path_file = 'variant/tests/files/test_variant.json'

        with open(path_file, 'r') as data_file:
            data_str = data_file.read()

        data_dict = json.loads(data_str)

        request = 'http://{host}:{port}/ws/variant/?test=True'.format(
                                                host=VariantWebServiceTestClass.HOST,
                                                port=VariantWebServiceTestClass.PORT)

        response = requests.post(request, json=data_dict)

        self.assertEqual(200, response.status_code)


    def test_find_variant_distinct_filters(self):
        """
        The web service for finding filters for a sample is checked
        """

        request = 'http://{host}:{port}/ws/variant/filters/{sample_name}/?test=True'.format(
                                                host=VariantWebServiceTestClass.HOST,
                                                port=VariantWebServiceTestClass.PORT,
                                                sample_name='splTOTO')
        response = requests.get(request)

        self.assertEqual(200, response.status_code)


    def test_find_variant_frequencies(self):
        """
        The web service for finding sample with a some frequency is checked
        """

        request = 'http://{host}:{port}/ws/variant/frequency/{sample_name}/{frequency}/{comparator}/?test=True'.format(
                                                host=VariantWebServiceTestClass.HOST,
                                                port=VariantWebServiceTestClass.PORT,
                                                sample_name='splTOTO',
                                                frequency=40,
                                                comparator=ComparatorEnum.GT.value)

        print((ComparatorEnum.GT).value)
        print(request)

        response = requests.get(request)

        self.assertEqual(200, response.status_code)

    def test_find_node_contains_value(self):
        """
        The web service for finding sample with some value for a specific node is checked
        """
        request = 'http://{host}:{port}/ws/variant/node_value/{sample_name}/{node}/{value}/?test=True'.format(
                                                host=VariantWebServiceTestClass.HOST,
                                                port=VariantWebServiceTestClass.PORT,
                                                sample_name='splTOTO',
                                                node='annot.changes.HGVSc',
                                                value='524G>A')

        response = requests.get(request)

        self.assertEqual(200, response.status_code)

