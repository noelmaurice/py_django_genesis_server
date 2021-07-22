import json

import requests
from rest_framework import status

from genesis.api.parentAPI import ParentAPI
from genesis.variant.model_data.variantData import Variant


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

            if response.status_code != status.HTTP_201_CREATED:
                raise Exception

        except Exception:
            raise Exception('VARIANT CREATE ERROR')

        return json.loads(response.text)

    @staticmethod
    def find_node_value(sample_name: str,
                        node: str,
                        value: str) -> [Variant]:

        ws_url_node_value = VariantAPI.WS_URL + "node_value/"

        response = requests.get("{ws_url}{sample_name}/{node}/{value}/".format(
            ws_url=ws_url_node_value,
            sample_name=sample_name,
            node=node,
            value=value))

        variants_json = json.loads(response.text)

        variants = [Variant.from_json(variant_json) for variant_json in variants_json]

        return variants

    @staticmethod
    def find_distinct_filters(sample_name) -> [str]:

        ws_url_filters = VariantAPI.WS_URL + "filters/"

        response = requests.get("{ws_url}{sample_name}/".format(
            ws_url=ws_url_filters,
            sample_name=sample_name))

        filters = json.loads(response.text)

        return filters

    @staticmethod
    def find_frequency(
            sample_name: str,
            frequency: float,
            comparator: str):

        ws_url_frequency = VariantAPI.WS_URL + "frequency/"

        response = requests.get("{ws_url}{sample_name}/{frequency}/{comparator}/".format(
            ws_url=ws_url_frequency,
            sample_name=sample_name,
            frequency=frequency,
            comparator=comparator))

        variants_json = json.loads(response.text)

        variants = [Variant.from_json(variant_json) for variant_json in variants_json]

        return variants
