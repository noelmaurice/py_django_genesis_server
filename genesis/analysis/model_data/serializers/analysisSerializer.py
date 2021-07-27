from rest_framework import serializers

from genesis.analysis.model_data.analysisData import Sample, SampleTag


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = '__all__'


class SampleTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleTag
        fields = '__all__'
