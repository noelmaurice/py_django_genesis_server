"""
Sample web services
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from genesis.analysis.model_data.serializers.analysisSerializer import SampleSerializer


class SampleView(APIView):
    """
    Requests on the samples
    """

    def post(self, request, *args, **kwargs):
        """
        Save the sample and return its id

        @param request: Request object with sample to record
        @param args: args attributes
        @param kwargs: kwargs attributes
        @return: The id of the sample saved
        """
        data = request.data
        serializer = SampleSerializer(data=data)
        if serializer.is_valid():
            sample = serializer.save()
            serializer = SampleSerializer(sample)

            result = {'id': serializer.data['id']}

            return Response(result, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)