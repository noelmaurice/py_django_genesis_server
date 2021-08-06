"""
Analysis web services
"""
from rest_framework.generics import ListCreateAPIView, CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from genesis.analysis.model_data.serializers.analysisSerializer import SampleSerializer
from rest_framework import mixins, status

from genesis.analysis.model_data.analysisData import *


class SampleList(ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class RunList(ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = Run.get_serializer()


class ResultList(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = Result.get_serializer()


class AnalysisList(ListCreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = Analysis.get_serializer()


class SampleDetail(RetrieveUpdateDestroyAPIView):
    """
    Create or update a sample.
    """
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    def post(self, request):
        serializer = SampleSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            sample = Sample.objects.get(pk=pk)
            parent = Sample.objects.get(pk=request.data['parent'])
        except:
            return Response({"detail": "The sample does not exist."}, status.HTTP_400_BAD_REQUEST)

        if parent.id != sample.id:
            sample.parent = parent
            sample.save()
        else:
            return Response({"detail": "A sample can not be its own parent."}, status.HTTP_400_BAD_REQUEST)

        data_json = SampleSerializer(sample)

        return Response(data_json.data, status.HTTP_200_OK)


class SampleTagDetail(CreateAPIView):
    queryset = SampleTag.objects.all()
    serializer_class = SampleTag.get_serializer()


class ProviderDetail(CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = Provider.get_serializer()


class InstrumentDetail(CreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = Instrument.get_serializer()


class RunDetail(RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = Run.get_serializer()


class RunTagDetail(CreateAPIView):
    queryset = RunTag.objects.all()
    serializer_class = RunTag.get_serializer()


class ResultDetail(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericAPIView):
    queryset = Result.objects.all()
    serializer_class = Result.get_serializer()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SoftwareDetail(CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = Software.get_serializer()


class AnalysisDetail(RetrieveUpdateDestroyAPIView):
    queryset = Analysis.objects.all()
    serializer_class = Analysis.get_serializer()


class ResultConsumerDetail(CreateAPIView):
    queryset = ResultConsumer.objects.all()
    serializer_class = ResultConsumer.get_serializer()


class SampleResultDetail(CreateAPIView):
    queryset = SampleResult.objects.all()
    serializer_class = SampleResult.get_serializer()


class RunSampleDetail(CreateAPIView):
    queryset = RunSample.objects.all()
    serializer_class = RunSample.get_serializer()
