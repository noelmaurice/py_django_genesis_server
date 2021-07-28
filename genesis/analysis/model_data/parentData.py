from rest_framework import serializers


class DataModel:
    """
    All the objects managed by django inherit of DataModel
    """

    TABLE_PREFIX = 'gen_'

    class Meta:
        abstract = True

    @classmethod
    def get_serializer(cls):
        class DataSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = '__all__'

        return DataSerializer
