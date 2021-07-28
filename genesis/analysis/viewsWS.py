"""
Analysis web services
"""

from rest_framework import generics
from genesis.analysis.model_data.serializers.analysisSerializer import *

class SampleDetail(generics.CreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleTagDetail(generics.CreateAPIView):
    queryset = SampleTag.objects.all()
    serializer_class = SampleTagSerializer


class ProviderDetail(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class InstrumentDetail(generics.CreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class RunDetail(generics.CreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer


class RunTagDetail(generics.CreateAPIView):
    queryset = RunTag.objects.all()
    serializer_class = RunTagSerializer


class ResultDetail(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class SoftwareDetail(generics.CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer


class AnalysisDetail(generics.CreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer


class ResultConsumerDetail(generics.CreateAPIView):
    queryset = ResultConsumer.objects.all()
    serializer_class = ResultConsumerSerializer


class SampleResultDetail(generics.CreateAPIView):
    queryset = SampleResult.objects.all()
    serializer_class = SampleResultSerializer


class RunSampleDetail(generics.CreateAPIView):
    queryset = RunSample.objects.all()
    serializer_class = RunSampleSerializer


