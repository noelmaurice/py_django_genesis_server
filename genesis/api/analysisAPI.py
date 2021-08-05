import json

import requests
from rest_framework import status

from genesis.api.parentAPI import ParentAPI


class SampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample/"

    @staticmethod
    def updateParentSampleWS(sample_id: int, parent_id: int) -> str:
        try:
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            url = SampleAPI.WS_URL + '{sample_id}/parent/'.format(
                sample_id = sample_id
                )

            data_json = {"parent": parent_id}

            response = requests.put(url, json=data_json, headers=headers)

            if response.status_code != status.HTTP_200_OK:
                raise Exception('STATUS CODE ERROR')

        except Exception as e:
            raise Exception('ERROR WHILE WEB SERVICE CALL', e.__str__())

        return json.loads(response.text)


class SampleTagAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample_tag/"


class RunAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/run/"


class RunTagAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/run_tag/"


class ProviderAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/provider/"


class InstrumentAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/instrument/"


class SoftwareAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/software/"


class ResultAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/result/"

    @staticmethod
    def updateResultWS(result_id: int, data_dict: dict) -> str:
        try:
            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }

            url = ResultAPI.WS_URL + '{result_id}/'.format(
                result_id=result_id
            )

            response = requests.put(url, json=data_dict, headers=headers)

            if response.status_code != status.HTTP_200_OK:
                raise Exception('STATUS CODE ERROR')

        except Exception as e:
            raise Exception('ERROR WHILE WEB SERVICE CALL', e.__str__())

        return json.loads(response.text)


class AnalysisAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/analysis/"


class RunSampleAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/run_sample/"


class ResultConsumerAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/result_consumer/"


class SampleResultAPI(ParentAPI):
    WS_URL = ParentAPI.WS_URL + "analysis/sample_result/"

