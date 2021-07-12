import json
from collections import namedtuple

import requests

from genesis.api.parentAPI import ParentAPI
from genesis.sample.model_data.sample import Sample, Part
from genesis.sample.model_data.serializers.sampleSerializer import SampleSerializer


class SampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "sample/"

    @staticmethod
    def test(id: int) -> Sample:

        response = requests.get(SampleAPI.WS_URL + str(id))

        data_json = response.text
        data_dict = json.loads(data_json)

        # sample: Sample = namedtuple("Sample", data_dict.keys())(*data_dict.values())
        s: Sample = Sample()
        s.name = data_dict.get('name')
        s.filters = data_dict.get('filters')

        values: [Part] = []
        for v in data_dict.get('values'):
            p: Part = Part()
            p.name = v['name']
            p.value = v['value']
            values.append(p)

        s.values = values

        test_sample: Sample = Sample()
        test = test_sample.from_json(data_dict)
        return test

    @staticmethod
    def read(id: int) -> SampleSerializer:

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
                # print(sample.values[0]['name'])
            else:
                raise Exception

        except Exception:
            raise Exception('SAMPLE READING ERROR')

        return sample

    @staticmethod
    def read(id: int) -> SampleSerializer:

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
                # print(sample.values[0]['name'])
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

            samples: [SampleSerializer] = []
            for sample_json in data_json:

                sampleSerializer: SampleSerializer = SampleSerializer(data=sample_json)

                if sampleSerializer.is_valid():
                    # sample_json: Sample = namedtuple("Sample", sample_json.keys())(*sample_json.values())
                    # samples.append(sample_json)

                    for sample in sampleSerializer.data:
                        samples.append(sample)
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
