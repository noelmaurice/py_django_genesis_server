from typing import TypeVar, Generic

from rest_framework import serializers

from genesis.analysis.model_data.analysisData import *


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = '__all__'


class SampleTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleTag
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = '__all__'


class RunSerializer(serializers.ModelSerializer):

    class Meta:
        model = Run
        fields = '__all__'


class RunTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = RunTag
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Software
        fields = '__all__'


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'


class ResultConsumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultConsumer
        fields = '__all__'


class SampleResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleResult
        fields = '__all__'


class RunSampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RunSample
        fields = '__all__'
