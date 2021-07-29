"""
Analysis data
See : https://docs.djangoproject.com/fr/3.2/ref/models/options/
"""


from django.db import models

from genesis.analysis.model_data.parentData import DataModel


class Sample(models.Model, DataModel):
    # sample name
    name = models.CharField(max_length=100)

    # date of the sample record
    creation_date = models.DateTimeField(null=True)

    # description of the sample
    description = models.CharField(max_length=300, null=True)

    # id of the sample parent, null otherwise
    parent = models.ForeignKey('self', models.DO_NOTHING, null=True)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample'

class SampleTag(models.Model, DataModel):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    sample = models.ForeignKey(Sample, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample_tag'


class Provider(models.Model, DataModel):
    description = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'provider'


class Instrument(models.Model, DataModel):
    acquisition_date = models.DateTimeField(null=True)
    model = models.CharField(max_length=50)
    provider_sn = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'instrument'


class Run(models.Model, DataModel):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    instrument = models.ForeignKey(Instrument, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run'


class RunTag(models.Model, DataModel):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250)
    type = models.CharField(max_length=10)
    run = models.ForeignKey(Run, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run_tag'


class Software(models.Model, DataModel):
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'software'


class Analysis(models.Model, DataModel):
    cmd = models.TextField(null=True)
    end_date = models.DateTimeField(null=True)
    software_version = models.CharField(max_length=50, null=True)
    start_date = models.DateTimeField(null=True)
    software = models.ForeignKey(Software, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'analysis'


class Result(models.Model, DataModel):
    category = models.CharField(max_length=50)
    path = models.CharField(max_length=300)
    tag = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    provider_analysis = models.ForeignKey(Analysis, models.DO_NOTHING, name='provider', null=True)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'result'


class ResultConsumer(models.Model, DataModel):
    result = models.ForeignKey(Result, models.DO_NOTHING)
    consumer_analyzes = models.ForeignKey(Analysis, models.DO_NOTHING, name='consumer', null=True)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'result_consumer'


class RunSample(models.Model, DataModel):
    run = models.ForeignKey(Run, models.DO_NOTHING)
    sample = models.ForeignKey(Sample, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'run_sample'


class SampleResult(models.Model, DataModel):
    sample = models.ForeignKey(Sample, models.DO_NOTHING)
    result = models.ForeignKey(Result, models.DO_NOTHING)

    class Meta:
        db_table = DataModel.TABLE_PREFIX + 'sample_result'



