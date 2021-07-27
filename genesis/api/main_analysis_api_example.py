import json
import os
from typing import Generic, TypeVar

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from genesis.api.analysisAPI import SampleAPI, SampleTagAPI

"""
SAMPLE CREATE WS
"""
print('SAMPLE CREATE WS')

data_json = '{"name": "splTOTO",\
                    "description": "Example of sample"}'

id_json: str = SampleAPI.create(data_json)
print(id_json, '\r\n')


"""
SAMPLE_TAG CREATE WS
"""
print('SAMPLE_TAG CREATE WS')

data_json = '{"key": "origin",\
                    "value": "anapath",\
                    "type": "str",\
                    "sample": 324}'

id_json: str = SampleTagAPI.create(data_json)
print(id_json, '\r\n')
