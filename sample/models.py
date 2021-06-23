from django.contrib.postgres.fields import ArrayField
from django.db import models


class Sample(models.Model):
    name = models.CharField(max_length=200, help_text='Sample name')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    filters = ArrayField(models.CharField(max_length=200, help_text='Filters'))

    class Meta:
        db_table = 'sample'

    def __str__(self):
        return self.name + ' (' + str(self.id) + ')'


class Part(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, help_text='Sample')
    name = models.CharField(max_length=200, help_text='Part name')
    value = models.CharField(max_length=200, help_text='Part value')

    class Meta:
        db_table = 'part'

    def __str__(self):
        return '{} - {}'.format(self.sample.name, self.name)
