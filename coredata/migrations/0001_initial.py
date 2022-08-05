    # Generated by Django 3.2.8 on 2022-01-05 05:23

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('name_ru', models.CharField(max_length=250, verbose_name='name_ru')),
                ('name_en', models.CharField(max_length=250)),
                ('name_uz', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'POTASSIUM_COEFFICIENT'), (2, 'PHOSPHORUS_COEFFICIENT'), (3, 'EXPENSE'), (4, 'ANOTHER')], default=4)),
                ('name_ru', models.CharField(max_length=512, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=512, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=512, null=True, verbose_name='Nomi')),
                ('status', models.BooleanField(default=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('val', models.DecimalField(decimal_places=4, max_digits=30, null=True, verbose_name='Qiymati')),
                ('potassium_val', models.DecimalField(decimal_places=4, default=0, max_digits=30, null=True, verbose_name='Kaliy Qiymati')),
                ('phosphorus_val', models.DecimalField(decimal_places=4, default=0, max_digits=30, null=True, verbose_name='Fosfor Qiymati')),
                ('nitrogen_val', models.DecimalField(decimal_places=4, default=0, max_digits=30, null=True, verbose_name='Azot Qiymati')),
                ('code', models.CharField(max_length=512, null=True, verbose_name='Kodi')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=512, verbose_name='Название регион')),
                ('name_en', models.CharField(max_length=512, verbose_name='Name of region')),
                ('name_uz', models.CharField(max_length=512, null=True, verbose_name='Viloyat nomi')),
                ('coefficient', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Regions',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=50, verbose_name='Название на русском')),
                ('name_en', models.CharField(max_length=50, verbose_name='Название на английском')),
                ('name_local', models.CharField(max_length=50, verbose_name='Местное название')),
                ('code', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='coredata.region', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_role', models.IntegerField(choices=[(0, 'ADMIN'), (1, 'SELLER'), (3, 'WAREHOUSE MANAGER'), (4, 'COLLECTOR'), (5, 'ACCOUNTANT'), (6, 'SHOP MANAGER'), (7, 'DELIVER')], default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]