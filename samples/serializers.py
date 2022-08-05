from rest_framework import serializers

from .models import Sample


class SampleSerializer(serializers.ModelSerializer):
    name_calculation_region = serializers.ReadOnlyField(source='calculation_region_name')
    name_creator = serializers.ReadOnlyField(source='creator_name')
    name_crop_type = serializers.ReadOnlyField(source='crop_type_name')
    inn_or_pinfl = serializers.IntegerField(required=True)

    class Meta:
        model = Sample
        fields = '__all__'
        extra_fields = ('name_calculation_region', 'name_creator', 'name_crop_type')
        read_only_fields = ('adder_district', 'creator')
        extra_kwargs = {
            'layer_width': {'required': True},
            'farm_name': {'required': True},
            'area_name': {'required': True}
        }
