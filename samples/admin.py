from django.contrib import admin


# Register your models here.
from samples.models import Sample


class SamplesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'calculation_region', 'creator', 'area')
    list_display_links = ('calculation_region',)


admin.site.register(Sample, SamplesAdmin)
