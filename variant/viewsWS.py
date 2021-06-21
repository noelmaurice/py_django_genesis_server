
from django.http import JsonResponse
from rest_framework.views import APIView

from variant.model_data.data.parentData import DataModel


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

        id = str(req.inserted_id)

        return JsonResponse({'id': id}, safe=False)
