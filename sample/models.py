
from django.db import models


class Sample(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        db_table = 'sample'


class Part(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    class Meta:
        db_table = 'part'
