from rest_framework import serializers

from genesis.analysis.model_data.analysisData import Sample


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('id', 'name', 'values', 'filters')

