# Generated by Django 3.2.8 on 2022-03-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coredata', '0008_auto_20220329_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coredata.district', verbose_name='District of point'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.IntegerField(choices=[(0, 'ADMIN'), (1, 'MANAGER'), (2, 'COLLECTOR')], default=2),
        ),
    ]
