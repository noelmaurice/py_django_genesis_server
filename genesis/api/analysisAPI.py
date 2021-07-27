import json

import requests

from genesis.api.parentAPI import ParentAPI


class SampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample/"

    @staticmethod
    def create(data_json) -> str:

        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(SampleAPI.WS_URL, data=data_json, headers=headers)

        except Exception as e:
            raise Exception('SAMPLE CREATE ERROR', e.__str__())

        return json.loads(response.text)


class SampleTagAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample_tag/"

    @staticmethod
    def create(data_json) -> str:

        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(SampleTagAPI.WS_URL, data=data_json, headers=headers)

        except Exception as e:
            raise Exception('SAMPLE_TAG CREATE ERROR', e.__str__())

        return json.loads(response.text)
