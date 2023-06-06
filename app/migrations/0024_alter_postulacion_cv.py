# Generated by Django 4.1.3 on 2023-06-04 00:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_postulacion_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='CVs', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], verbose_name='Adjuntar CV'),
        ),
    ]
