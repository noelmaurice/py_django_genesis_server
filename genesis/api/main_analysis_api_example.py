import json
import os

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from genesis.api.analysisAPI import SampleAnalysisAPI

"""
SAMPLE CREATE WS
"""
print('SAMPLE CREATE WS')

data_json = "{'name': 'splTOTO', 'description': 'Example of sample'}"

id_json: str = SampleAnalysisAPI.create(data_json)
print(id_json, '\r\n')


