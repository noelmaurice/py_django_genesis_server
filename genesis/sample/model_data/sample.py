from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

from genesis.sample.model_data.parentData import DataModel


class Sample(models.Model, DataModel):

    # sample name
    name = models.CharField(max_length=200, help_text='Sample name')
    # publication date
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    # filter list of the sample
    filters = ArrayField(models.CharField(max_length=200, help_text='Filters'))

    class Meta:
        db_table = 'sample'

    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'

    @classmethod
    def from_json(cls, data: dict):
        sample: Sample = Sample()
        sample.name = data.get('name')
        sample.pub_date = data.get('pub_date')
        sample.filters = data.get('filters')

        values: [Part] = []
        for p in data.get('values'):
            part: Part = Part()
            values.append(part.from_json(p))

        sample.values = values

        return sample

class Part(models.Model, DataModel):

    # the related sample object
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, help_text='Sample')

    # part name
    name = models.CharField(max_length=200, help_text='Part name')

    # value for the part
    value = models.CharField(max_length=200, help_text='Part value')

    class Meta:
        db_table = 'part'

    def __str__(self):
        return '{} - {}'.format(self.sample.name, self.name)

    @classmethod
    def from_json(cls, data: dict):

        part: Part = Part()
        part.name = data.get('name')
        part.value = data.get('value')

        return part

