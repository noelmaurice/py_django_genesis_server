"""
Analysis data
See : https://docs.djangoproject.com/fr/3.2/ref/models/options/
"""


from django.db import models

from genesis.analysis.model_data.parentData import DataModel


class Sample(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample'


class SampleTag(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    sample = models.ForeignKey(Sample, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample_tag'


class Provider(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'provider'


class Instrument(models.Model):
    acquisition_date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=50)
    provider_sn = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'instrument'


class Run(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    instrument = models.ForeignKey(Instrument, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run'


class RunTag(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    run = models.ForeignKey(Run, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run_tag'


class Software(models.Model):
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'software'


class Analysis(models.Model, DataModel):
    cmd = models.CharField(max_length=5000)
    end_date = models.DateTimeField(auto_now_add=True)
    software_version = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    software = models.ForeignKey(Software, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'analysis'


class Result(models.Model):
    category = models.CharField(max_length=50)
    path = models.CharField(max_length=300)
    tag = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    provider_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, name='provider')

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'result'


class ResultConsumer(models.Model):
    result = models.ForeignKey(Result, models.DO_NOTHING)
    consumer_analyzes = models.ForeignKey(Analysis, models.DO_NOTHING, name='consumer')

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'result_consumer'


class RunSample(models.Model):
    run = models.ForeignKey(Run, models.DO_NOTHING)
    sample = models.ForeignKey(Sample, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run_sample'

class SampleResult(models.Model):
    sample = models.ForeignKey(Sample, models.DO_NOTHING)
    result = models.ForeignKey(Result, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample_result'
