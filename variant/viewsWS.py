
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from variant.model_data.data.parentData import DataModel
from variant.model_data.repository.variantRepository import VariantRepository


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


@api_view(['GET'])
def find_distinct_filters(request, sample_name):

    filters = VariantRepository.find_distinct_filters(
        sample_name,
        collect = DataModel.get_collect())

    return JsonResponse({'filters': filters}, safe=False)


@api_view(['GET'])
def find_node_contains_value(request,
        sample_name: str,
        node: str,
        value: str):
    """
    Search variants with the value for the variant node

    @param sample_name: Sample name
    @param node: The node on which the search is made
    @param value: The searched value for the node
    @param test: Test mode
    @return: The variants found
    @rtype: list(Variant)
    """
    variants = VariantRepository.find_variants_node_value(
        sample_name,
        node, [value],
        collect = DataModel.get_collect())

    return JsonResponse({}, safe=False)

@api_view(['GET'])
def find_variants_with_frequency(request,
         sample_name: str,
         frequency: str,
         operator: str):
    """
    Search the variant in accordance with the frequency value

    @param sample_name: Sample name
    @param frequency: The frequency value searched
    @param operator: The comparison operator
    @param test: Mode test
    @return: The variants found
    @rtype: list(Variant)
    """
    variants = VariantRepository.find_variants_frequency(
        sample_name,
        frequency,
        operator,
        collect = DataModel.get_collect())

    return JsonResponse({}, safe=False)
