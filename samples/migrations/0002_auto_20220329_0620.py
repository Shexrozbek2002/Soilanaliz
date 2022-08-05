# Generated by Django 3.2.8 on 2022-03-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='farm_name',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='inn_or_pinfl',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='layer_width',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sample',
            name='outline_number',
            field=models.TextField(default='', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_number',
            field=models.TextField(max_length=225, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set(),
        ),
    ]
