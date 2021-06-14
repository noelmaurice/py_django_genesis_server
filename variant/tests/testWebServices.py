"""
Testing variant data with database
"""
import json
from pprint import pprint

import requests

from variant.models.repository.repositoryModel import BaseComparator
from variant.tests.parentTest import ParentTest
from variant.models.repository.variantRepository import VariantRepository
from variant.web_services import mainScriptWS
from variant.web_services.data.variantWS import VariantWS


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
        path_file = 'variant/tests/files/test_variant.json'

        with open(path_file, 'r') as data_file:
            data_json = data_file.read()


        print(data_json)

        # data_dict = json.loads(data_json)
        #
        # data_json = json.dumps(data_json, default=lambda o: o.__dict__)
        # data_dict = json.loads(data_json)
        #
        # pprint(data_json)

        request = 'http://{}:{}/variant/?test=True'.format(mainScriptWS.HOST,
                                                           mainScriptWS.PORT)

        response = requests.post(request, data=data_json)

        self.assertEqual(200, response.status_code)


    def test_find_variant_distinct_filters(self):
        """
        The request for find filters for a sample is checked
        """

        request = 'http://{}:{}/variant/filters/?sample_name={}&test=True'.format(mainScriptWS.HOST,
                                                                        mainScriptWS.PORT,
                                                                        'splTOTO')
        response = requests.get(request)

        self.assertEqual(200, response.status_code)


    def test_find_variant_frequencies(self):
        """
        The request for find filters for a sample is checked
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
        request = 'http://{}:{}/variant/node_value/?sample_name={}&node={}&value={}&test=True'.format(
                                                                                        mainScriptWS.HOST,
                                                                                        mainScriptWS.PORT,
                                                                                        'splTOTO',
                                                                                        'annot.changes.HGVSc',
                                                                                        '524G>A')

        response = requests.get(request)

        self.assertEqual(200, response.status_code)

