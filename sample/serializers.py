from rest_framework import serializers

from sample.models import Sample, Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name', 'value')


class SampleSerializer(serializers.ModelSerializer):
    part_set = PartSerializer(many=True)

    class Meta:
        model = Sample
        fields = ('id', 'name', 'part_set')


    # the object and the nested objects are saved
    def create(self, validated_data):

        # the parts are removed of the validated_data and are saved in the part list
        part_validated_data = validated_data.pop('part_set')

        # the sample without parts is saved on the database
        sample = Sample.objects.create(**validated_data)

        # for each part object of the part list
        for each in part_validated_data:
            # the sample object added to the part object
            each['sample'] = sample

        # the part object serializer is instantiated
        part_set_serializer = self.fields['part_set']

        # the part objects of the part list are saved into database
        parts = part_set_serializer.create(part_validated_data)

        # the sample without parts is returned
        return sample

