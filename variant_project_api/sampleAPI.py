import json
from collections import namedtuple

import requests
from sample.model_data.sample import Sample
from sample.model_data.serializers.sampleSerializer import SampleSerializer

from variant_project_api.parentAPI import ParentAPI


class SampleAPI(ParentAPI):

    WS_URL = ParentAPI.WS_URL + "sample/"

    @staticmethod
    def read(id: int) -> Sample:

        try:
            response = requests.get(SampleAPI.WS_URL + str(id))

            data_json = response.json()

            if response.status_code != 200:
                raise Exception

            serializer: SampleSerializer = SampleSerializer(data=data_json)

            if serializer.is_valid():
                # print(serializer.data)
                sample: Sample = namedtuple("Sample", data_json.keys())(*data_json.values())
                # print(sample.name)
                # print(sample.filters)
                # print(sample.values)
                # print(*((item['name'], item['value']) for item in sample.values))
                # print(object_name.values[0]['name'])
            else:
                raise Exception


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

                serializer: SampleSerializer = SampleSerializer(data=sample_json)

                if serializer.is_valid():
                    sample_json: Sample = namedtuple("Sample", sample_json.keys())(*sample_json.values())
                    samples.append(sample_json)
                else:
                    raise Exception


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

