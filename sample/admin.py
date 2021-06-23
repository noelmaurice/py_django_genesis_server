
from django.contrib import admin

from sample.models import Sample, Part

# custom the model display on the admin site interface
@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    fields = ('name', 'filters', )

    # display the fields with read only mode
    # readonly_fields = ('pub_date')

    # add a nav bar on top
    # save_on_top = True

    # the autocompletion will be possible on the following search fields
    search_fields = ['name', 'filters', ]

    list_display = ('id', 'name', 'format_pub_date', )

    # fields editabled
    # list_editable = ('name', )

    list_filter = ('name', )

    def format_pub_date(self, sample: Sample):
        print(type(sample.pub_date))
        print(sample.pub_date.strftime("%b %d %Y"))
        return sample.pub_date.strftime("%d %b %Y")
    format_pub_date.short_description = 'Publication date'
    format_pub_date.admin_order_field = 'Publication date'

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):

    # all fields but not excluded fields
    # exclude = ('value', )

    # the autocompletion will be allowed for the following attribute :
    # see search_fields value of the linked attribute object
    autocomplete_fields = ['sample']

    list_display = ('name', 'value', 'sample', )

    search_fields = ('name', 'sample__name',)

    list_filter = ('name', )