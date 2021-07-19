from django.contrib import admin

"""
Sample administration
"""

from genesis.analysis.model_data.sample import Sample


# custom the model display on the admin site interface
@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    fields = ('name', 'filters',)

    # display the fields with read only mode
    # readonly_fields = ('pub_date')

    # add a nav bar on top
    # save_on_top = True

    # the autocompletion will be possible on the following search fields
    search_fields = ['name', 'filters', ]

    list_display = ('id', 'name', 'format_pub_date',)

    # fields editabled
    # list_editable = ('name', )

    list_filter = ('name',)

    def format_pub_date(self, sample: Sample):
        print(type(sample.pub_date))
        print(sample.pub_date.strftime("%b %d %Y"))
        return sample.pub_date.strftime("%d %b %Y")

    format_pub_date.short_description = 'Publication date'
    format_pub_date.admin_order_field = 'Publication date'
