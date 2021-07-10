import json

import requests
from variant.model_data.variant import Variant

from variant_project_api.api.parentAPI import ParentAPI


class VariantAPI(ParentAPI):

    WS_URL = ParentAPI.WS_URL + "variant/"

    @staticmethod
    def create(data_json: str) -> str:

        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(VariantAPI.WS_URL, data=data_json, headers=headers)

            if response.status_code != 200:
                raise Exception

        except Exception:
            raise Exception('VARIANT CREATE ERROR')

        return json.loads(response.text)


    @staticmethod
    def find_node_value(sample_name: str,
                        node: str,
                        value: str) -> [Variant]:

        ws_url_node_value = VariantAPI.WS_URL + "node_value/"

        response = requests.get("{WS_URL}{SAMPLE_NAME}/{NODE}/{VALUE}/".format(
                                                                WS_URL = ws_url_node_value,
                                                                SAMPLE_NAME = sample_name,
                                                                NODE = node,
                                                                VALUE = value))
        variants_json = json.loads(response.text)

        variants = [Variant.from_json(variant_json) for variant_json in variants_json]

        return variants

    @staticmethod
    def find_distinct_filters(sample_name) -> [str]:

        ws_url_filters = VariantAPI.WS_URL + "filters/"

        response = requests.get("{WS_URL}{SAMPLE_NAME}/".format(
                                                                WS_URL = ws_url_filters,
                                                                SAMPLE_NAME = sample_name))
        filters = json.loads(response.text)

        return filters

    @staticmethod
    def find_frequency(
                       sample_name: str,
                       frequency: float,
                       comparator: str):

        ws_url_frequency = VariantAPI.WS_URL + "frequency/"

        response = requests.get("{WS_URL}{SAMPLE_NAME}/{FREQUENCY}/{COMPARATOR}/".format(
                                                        WS_URL=ws_url_frequency,
                                                        SAMPLE_NAME=sample_name,
                                                        FREQUENCY=frequency,
                                                        COMPARATOR=comparator))
        variants_json = json.loads(response.text)

        variants = [Variant.from_json(variant_json) for variant_json in variants_json]

        return variants

