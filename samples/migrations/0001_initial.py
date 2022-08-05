# Generated by Django 3.2.8 on 2022-02-01 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coredata', '0004_region_limit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_nitrogen', models.DecimalField(decimal_places=3, max_digits=20)),
                ('given_phosphorus', models.DecimalField(decimal_places=3, max_digits=20)),
                ('given_potassium', models.DecimalField(decimal_places=3, max_digits=20)),
                ('given_humus', models.DecimalField(decimal_places=3, max_digits=20)),
                ('provided_level_phosphorus', models.CharField(choices=[('LOW', 'Low'), ('LOWEST', 'Lowest'), ('NORMAL', 'Normal'), ('HIGH', 'High'), ('HIGHEST', 'Highest')], max_length=12)),
                ('provided_level_potassium', models.CharField(choices=[('LOW', 'Low'), ('LOWEST', 'Lowest'), ('NORMAL', 'Normal'), ('HIGH', 'High'), ('HIGHEST', 'Highest')], max_length=12)),
                ('provided_level_humus', models.CharField(choices=[('LOW', 'Low'), ('LOWEST', 'Lowest'), ('NORMAL', 'Normal'), ('HIGH', 'High'), ('HIGHEST', 'Highest')], max_length=12)),
                ('provided_level_nitrogen', models.CharField(choices=[('LOW', 'Low'), ('LOWEST', 'Lowest'), ('NORMAL', 'Normal'), ('HIGH', 'High'), ('HIGHEST', 'Highest')], max_length=12)),
                ('coefficient_nitrogen', models.DecimalField(decimal_places=4, max_digits=20)),
                ('coefficient_phosphorus', models.DecimalField(decimal_places=4, max_digits=20)),
                ('coefficient_potassium', models.DecimalField(decimal_places=4, max_digits=20)),
                ('usage_per_centner_nitrogen', models.DecimalField(decimal_places=4, max_digits=20)),
                ('usage_per_centner_phosphorus', models.DecimalField(decimal_places=4, max_digits=20)),
                ('usage_per_centner_potassium', models.DecimalField(decimal_places=4, max_digits=20)),
                ('usage_per_centner_humus', models.DecimalField(decimal_places=4, max_digits=20)),
                ('area', models.DecimalField(decimal_places=2, max_digits=20)),
                ('outline_number', models.TextField(default='', max_length=225, null=True)),
                ('sample_number', models.TextField(max_length=225)),
                ('added_at', models.DateField(auto_now_add=True, verbose_name='added at')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('calculation_district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calculation_district', to='coredata.district', verbose_name='Calculation District')),
                ('calculation_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calculation_region', to='coredata.region', verbose_name='Calculation Region')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='samples', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('crop_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_type', to='coredata.reference', verbose_name='Crop Type')),
            ],
            options={
                'ordering': ['-added_at'],
                'unique_together': {('outline_number', 'sample_number')},
            },
        ),
    ]