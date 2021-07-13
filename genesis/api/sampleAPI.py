import json

import requests

from genesis.api.parentAPI import ParentAPI
from genesis.sample.model_data.sample import Sample


class SampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "sample/"

    @staticmethod
    def read(id: int) -> Sample:

        try:
            response = requests.get(SampleAPI.WS_URL + str(id))

            if response.status_code != 200:
                raise Exception

            data_json = response.text
            data_dict = json.loads(data_json)

            sample = Sample.from_json(data_dict)

        except Exception:
            raise Exception('SAMPLE READING ERROR')

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

        except Exception:
            raise Exception('ALL SAMPLE READING ERROR')

        return samples

    @staticmethod
    def create(data_json) -> str:

        try:

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            response = requests.post(SampleAPI.WS_URL, data=data_json, headers=headers)

            if response.status_code != 201:
                raise Exception

        except Exception:
            raise Exception('SAMPLE CREATE ERROR')

        return json.loads(response.text)
