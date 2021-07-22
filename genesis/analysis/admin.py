"""
Analysis administration site
See : https://docs.djangoproject.com/fr/3.2/ref/contrib/admin/
"""

from django.contrib import admin

from genesis.analysis.model_data.analysisData import *

# custom the model display on the admin site interface
@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    pass


@admin.register(SampleTag)
class SampleTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    pass


@admin.register(RunTag)
class RunTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    pass



@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'analysis'
        verbose_name_plural = 'analyzes'


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass



@admin.register(ResultConsumer)
class ResultConsumerAdmin(admin.ModelAdmin):
    pass


@admin.register(RunSample)
class RunSampleAdmin(admin.ModelAdmin):
    pass


@admin.register(SampleResult)
class SampleResultAdmin(admin.ModelAdmin):
    pass