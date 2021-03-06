"""
Variant web services
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from genesis.variant.model_data.parentData import DataModel
from genesis.variant.model_data.repository.variantRepository import VariantRepository
from genesis.variant.tests.parentTest import ParentTest


class VariantView(APIView):
    """
    Requests on the variants
    """

    @staticmethod
    def post(request,
             *args,
             **kwargs):
        """
        Save the variant and return its ID

        @param request: Request object with variant to record
        @param args: args attributes
        @param kwargs: kwargs attributes
        @return: The ID saved variant
        """

        try:
            if ('test' in request.query_params) and (request.query_params['test'] == 'True'):
                collect = ParentTest.get_test_collect()
            else:
                collect = DataModel.get_collect()

            req = collect.insert_one(request.data)

            id = str(req.inserted_id)

        except Exception:
            raise Exception('Error while the web service call')

        return Response({'id': id}, status=status.HTTP_201_CREATED)

    @staticmethod
    @api_view(['GET'])
    def find_distinct_filters(request,
                              sample_name):
        """
        Search the filters of the sample
        @param request: Request object
        @param sample_name: Sample name
        @return: The filter list of the sample
        """
        try:
            if ('test' in request.query_params) and (request.query_params['test'] == 'True'):
                collect = ParentTest.get_test_collect()
            else:
                collect = DataModel.get_collect()

            filters = VariantRepository.find_distinct_filters(
                sample_name,
                collect)

        except Exception:
            raise Exception('Error while the web service call')

        return Response({'filters': filters})

    @staticmethod
    @api_view(['GET'])
    def find_node_value(request,
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

        try:

            if ('test' in request.query_params) and (request.query_params['test'] == 'True'):
                collect = ParentTest.get_test_collect()
            else:
                collect = DataModel.get_collect()

            variants = VariantRepository.find_variants_node_value(
                sample_name,
                node, [value],
                collect)

        except Exception:
            raise Exception('Error while the web service call')

        return Response(variants)

    @staticmethod
    @api_view(['GET'])
    def find_frequency(request,
                       sample_name: str,
                       frequency: float,
                       comparator: str):
        """
        Search the variant in accordance with the frequency value

        @param sample_name: Sample name
        @param frequency: The frequency value searched
        @param comparator: The comparison operator
        @param test: Mode test
        @return: The variants found
        @rtype: list(Variant)
        """

        try:





            if ('test' in request.query_params) and (request.query_params['test'] == 'True'):
                collect = ParentTest.get_test_collect()
            else:
                collect = DataModel.get_collect()
            variable = 'toto'
            variants = VariantRepository.find_variants_frequency(sample_name,
                                                                 frequency,
                                                                 comparator,
                                                                 collect)
        except Exception:
            raise Exception('Error while the web service call')

        return Response(variants)
