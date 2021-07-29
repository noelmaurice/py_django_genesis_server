
"""
The specific serializers can be defined below.

The DataModel class implements a generic serializer used in the most cases.
"""
from genesis.analysis.model_data.analysisData import Sample
from rest_framework import serializers


class SampleSerializer(serializers.ModelSerializer):
    # the related parts of the sample

    class Meta:
        model = Sample
        fields = '__all__'