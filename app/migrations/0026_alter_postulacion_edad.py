# Generated by Django 4.1.3 on 2023-06-04 00:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_postulacion_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18, message='No puedes postular siendo menor de edad'), django.core.validators.MaxValueValidator(100, message='La edad no puede ser mayor a 100.')], verbose_name='Edad'),
        ),
    ]
