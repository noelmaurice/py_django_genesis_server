import json
from pprint import pprint

from django.http import JsonResponse
from requests import Response
from rest_framework.views import APIView

from variant.model_data.data.parentData import DataModel
from variant.model_data.data.variant import Variant
from variant.model_data.repository.variantRepository import VariantRepository
from variant.web_services.data.variantWS import VariantWS
from variant.web_services.mainScriptWS import get_collection


class VariantView(APIView):
    """
        The variant is saved in the database

        @param variant_ws: Variant to save
        @param test: Test mode
        @return: Id of the variant saved
        @rtype: str
        """

    def post(self, request, *args, **kwargs):

        collect = DataModel.get_collect()
        req = collect.insert_one(request.data)

        return JsonResponse({'id': str(req.inserted_id)}, safe=False)
