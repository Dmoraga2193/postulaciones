# Generated by Django 4.1.3 on 2023-06-03 22:13

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_postulacion_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='celular',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Ej: +56945216387', max_length=128, region=None, verbose_name='Celular'),
        ),
    ]
