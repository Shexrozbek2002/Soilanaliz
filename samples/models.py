from django.db import models

# Create your models here.
from coredata.models import District, User, Reference, Region


class Sample(models.Model):
    class Status(models.TextChoices):
        low = 'LOW', 'Low'
        lowest = 'LOWEST', 'Lowest'
        normal = 'NORMAL', 'Normal'
        high = 'HIGH', 'High'
        highest = 'HIGHEST', 'Highest'

    given_nitrogen = models.DecimalField(max_digits=20, decimal_places=3)
    given_phosphorus = models.DecimalField(max_digits=20, decimal_places=3)
    given_potassium = models.DecimalField(max_digits=20, decimal_places=3)
    given_humus = models.DecimalField(max_digits=20, decimal_places=3)
    provided_level_phosphorus = models.CharField(
        choices=Status.choices,
        max_length=12,
    )
    provided_level_potassium = models.CharField(
        choices=Status.choices,
        max_length=12,
    )
    provided_level_humus = models.CharField(
        choices=Status.choices,
        max_length=12,
    )
    provided_level_nitrogen = models.CharField(
        choices=Status.choices,
        max_length=12,
    )
    coefficient_nitrogen = models.DecimalField(max_digits=20, decimal_places=4)
    coefficient_phosphorus = models.DecimalField(max_digits=20, decimal_places=4)
    coefficient_potassium = models.DecimalField(max_digits=20, decimal_places=4)
    usage_per_centner_nitrogen = models.DecimalField(max_digits=20, decimal_places=4)
    usage_per_centner_phosphorus = models.DecimalField(max_digits=20, decimal_places=4)
    usage_per_centner_potassium = models.DecimalField(max_digits=20, decimal_places=4)
    usage_per_centner_humus = models.DecimalField(max_digits=20, decimal_places=4)
    area = models.DecimalField(max_digits=20, decimal_places=2)
    outline_number = models.TextField(max_length=225, unique=True, default='')
    sample_number = models.TextField(max_length=225, unique=True, null=False)
    calculation_region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL,
                                           verbose_name='Calculation Region', related_name='calculation_region')
    calculation_district = models.ForeignKey(District, null=True, on_delete=models.SET_NULL,
                                             verbose_name='Calculation District', related_name='calculation_district')
    crop_type = models.ForeignKey(Reference, null=True, on_delete=models.SET_NULL, verbose_name='Crop Type',
                                  related_name='crop_type')
    added_at = models.DateField(auto_now_add=True, verbose_name='added at', editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Creator',
                                related_name='samples')
    area_name = models.CharField(max_length=225, null=True)
    layer_width = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    farm_name = models.CharField(max_length=225, null=True)
    inn_or_pinfl = models.CharField(max_length=30, null=True)


    @property
    def calculation_region_name(self):
        if self.calculation_region:
            return self.calculation_region.name_uz
        else:
            return 'None region for this field'

    @property
    def creator_name(self):
        if self.creator:
            return self.creator.username
        else:
            return 'None user for this field'

    @property
    def crop_type_name(self):
        if self.crop_type:
            return self.crop_type.name_uz
        else:
            return 'None crop for this field'

    class Meta:
        ordering = ['-added_at']
