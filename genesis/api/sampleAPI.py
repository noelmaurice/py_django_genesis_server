import json

import requests
from rest_framework import status

from genesis.api.parentAPI import ParentAPI
from genesis.sample.model_data.sampleData import Sample


class SampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "sample/"

    @staticmethod
    def read(id: int) -> Sample:

        try:
            response = requests.get(SampleAPI.WS_URL + str(id))

            data_json = response.text
            data_dict = json.loads(data_json)

            sample = Sample.from_json(data_dict)

        except Exception as e:
            raise Exception('SAMPLE READING ERROR', e.__str__())

        return sample

    @staticmethod
    def read_all() -> [Sample]:

        try:
            response = requests.get(SampleAPI.WS_URL)

            data_json = response.json()

            if response.status_code != 200:
                raise Exception

            samples: [Sample] = []
            for sample_json in data_json:
                sample = Sample.from_json(sample_json)
                samples.append(sample)

        except Exception as e:
            raise Exception('ALL SAMPLE READING ERROR', e.__str__())

        return samples

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
