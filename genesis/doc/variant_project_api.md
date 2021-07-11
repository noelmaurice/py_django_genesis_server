# variant_project API

## DO QUERIES TO THE variant_project SERVER

>This API allows to do requests to the variant_project server thanks a simple python script and without know the server structure.
> 
>First to all, the python library must be imported in the python environment with the **pip install library_name** command.
>
>Then, a simple python script is enough to query the variant project server.
> 
>A implementation example script for doing requests to the server is available below.

### SOURCE CODE EXAMPLE

**CAUTION: This example does not present all the possibilities of the API**

```py
import json
from collections import namedtuple

import requests
from genesis.sample.model_data.sample import Sample
from genesis.sample.model_data.serializers.sampleSerializer import SampleSerializer

from genesis.api.parentAPI import ParentAPI


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
```