# Generated by Django 3.0.8 on 2020-10-02 22:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0003_auto_20201002_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqiprediction',
            name='Atmospheric_Pressure',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1050)]),
        ),
    ]
