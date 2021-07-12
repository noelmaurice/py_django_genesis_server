from django.contrib.postgres.fields import ArrayField
from genesis.sample.model_data.sample import Part, Sample
from rest_framework import serializers


class Part2Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, help_text='Part name')
    value = serializers.CharField(max_length=200, help_text='Part value')

    class Meta:
        model = Part
        fields = ('id', 'name', 'value')

class Sample2Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, help_text='Sample name')
    pub_date = serializers.DateTimeField('date published')
    filters = ArrayField(serializers.CharField(max_length=200, help_text='Filters'))
    values = Part2Serializer()

    class Meta:
        model = Sample
        fields = ('id', 'name', 'values', 'filters')

