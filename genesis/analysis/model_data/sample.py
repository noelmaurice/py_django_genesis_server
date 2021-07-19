from django.contrib.postgres.fields import ArrayField
from django.db import models

from genesis.analysis.model_data.parentData import DataModel


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
