"""
Analysis web services
"""
import json
from pprint import pprint

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from genesis.analysis.model_data.serializers.analysisSerializer import SampleSerializer
from rest_framework import generics, mixins, status

from genesis.analysis.model_data.analysisData import *


class SampleDetail(APIView):
    """
    Create or update a sample.
    """
    def post(self, request):
        serializer = SampleSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, parent_id):
        sample = Sample.objects.get(pk=pk)
        parent = Sample.objects.get(pk=parent_id)

        if parent.id != sample.id:
            sample.parent = parent
            sample.save()

        else:
            raise Exception('THE SAMPLE CAN NOT HAVE THIS PARENT SAMPLE')

        data_json = SampleSerializer(sample)

        return Response(data_json.data, status.HTTP_200_OK)


class SampleTagDetail(generics.CreateAPIView):
    queryset = SampleTag.objects.all()
    serializer_class = SampleTag.get_serializer()


class ProviderDetail(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = Provider.get_serializer()


class InstrumentDetail(generics.CreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = Instrument.get_serializer()


class RunDetail(generics.CreateAPIView):
    queryset = Run.objects.all()
    serializer_class = Run.get_serializer()


class RunTagDetail(generics.CreateAPIView):
    queryset = RunTag.objects.all()
    serializer_class = RunTag.get_serializer()


class ResultDetail(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    queryset = Result.objects.all()
    serializer_class = Result.get_serializer()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SoftwareDetail(generics.CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = Software.get_serializer()


class AnalysisDetail(generics.CreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = Analysis.get_serializer()


class ResultConsumerDetail(generics.CreateAPIView):
    queryset = ResultConsumer.objects.all()
    serializer_class = ResultConsumer.get_serializer()


class SampleResultDetail(generics.CreateAPIView):
    queryset = SampleResult.objects.all()
    serializer_class = SampleResult.get_serializer()


class RunSampleDetail(generics.CreateAPIView):
    queryset = RunSample.objects.all()
    serializer_class = RunSample.get_serializer()
