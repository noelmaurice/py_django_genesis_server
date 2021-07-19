from rest_framework import serializers

from genesis.analysis.model_data.sample import Sample


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ('id', 'name', 'values', 'filters')

