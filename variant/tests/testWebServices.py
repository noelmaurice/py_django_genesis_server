"""
Testing variant data with database
"""

import requests

from variant.models.repository.parentRepository import BaseComparator
from variant.tests.parentTest import ParentTest
from variant.web_services import mainScriptWS


class VariantWebServiceTestClass(ParentTest):
    """
    Class for testing the web services.

    For each test, only the request status of the web service is tested because the repository used is tested
    by the data model tests.
    """

    HOST = mainScriptWS.HOST
    PORT = str(mainScriptWS.PORT)

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
            data_json = data_file.read()

        request = 'http://{}:{}/variant/?test=True'.format(mainScriptWS.HOST,
                                                           mainScriptWS.PORT)

        response = requests.post(request, data=data_json)

        self.assertEqual(200, response.status_code)


    def test_find_variant_distinct_filters(self):
        """
        The web service for finding filters for a sample is checked
        """

        request = 'http://{}:{}/variant/filters/?sample_name={}&test=True'.format(mainScriptWS.HOST,
                                                                        mainScriptWS.PORT,
                                                                        'splTOTO')
        response = requests.get(request)

        self.assertEqual(200, response.status_code)


    def test_find_variant_frequencies(self):
        """
        The web service for finding sample with a some frequency is checked
        """

        request = 'http://{}:{}/variant/filters/?sample_name={}&frequency={}&operator={}&test=True'.format(
                                                                                                mainScriptWS.HOST,
                                                                                                mainScriptWS.PORT,
                                                                                                'splTOTO',
                                                                                                40,
                                                                                                BaseComparator.GT)

        response = requests.get(request)

        self.assertEqual(200, response.status_code)

    def test_find_node_contains_value(self):
        """
        The web service for finding sample with some value for a specific node is checked
        """
        request = 'http://{}:{}/variant/node_value/?sample_name={}&node={}&value={}&test=True'.format(
                                                                                        mainScriptWS.HOST,
                                                                                        mainScriptWS.PORT,
                                                                                        'splTOTO',
                                                                                        'annot.changes.HGVSc',
                                                                                        '524G>A')

        response = requests.get(request)

        self.assertEqual(200, response.status_code)

