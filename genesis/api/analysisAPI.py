import json

import requests
from rest_framework import status

from genesis.api.parentAPI import ParentAPI
from genesis.sample.model_data.sampleData import Sample


class SampleAnalysisAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample/"

    @staticmethod
    def create(data_json) -> str:

        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(SampleAnalysisAPI.WS_URL, data=data_json, headers=headers)

            if response.status_code != status.HTTP_201_CREATED:
                raise Exception

        except Exception:
            raise Exception('SAMPLE CREATE ERROR')

        return json.loads(response.text)
