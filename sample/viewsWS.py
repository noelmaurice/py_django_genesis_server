
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sample.models import Sample
from sample.serializers import SampleSerializer, PartSerializer


class SampleView(APIView):

    def get(self, request, format=None):
        samples = Sample.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            sample = serializer.save()
            serializer = SampleSerializer(sample)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
