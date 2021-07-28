"""
Analysis web services
"""

from rest_framework import generics, mixins

from genesis.analysis.model_data.analysisData import *


class SampleDetail(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = Sample.objects.all()
    serializer_class = Sample.get_serializer()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

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
