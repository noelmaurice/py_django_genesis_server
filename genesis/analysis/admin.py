from django.contrib import admin

"""
Sample administration
"""

from genesis.analysis.model_data.analysis import Analysis


# custom the model display on the admin site interface
@admin.register(Analysis)
class SampleAdmin(admin.ModelAdmin):
    pass
