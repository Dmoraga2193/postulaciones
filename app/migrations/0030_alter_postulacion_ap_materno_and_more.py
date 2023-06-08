# Generated by Django 4.1.3 on 2023-06-07 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_postulacion_ap_materno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='ap_materno',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El apellido solo debe contener letras', regex='^[a-zA-Z]*$')], verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='postulacion',
            name='ap_paterno',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El apellido solo debe contener letras', regex='^[a-zA-Z]*$')], verbose_name='Apellido Paterno'),
        ),
    ]