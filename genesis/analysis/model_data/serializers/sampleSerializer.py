from rest_framework import serializers

from genesis.analysis.model_data.analysis import Sample


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('id', 'name', 'values', 'filters')

