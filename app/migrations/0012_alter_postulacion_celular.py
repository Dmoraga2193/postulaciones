# Generated by Django 4.1.3 on 2023-06-03 22:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_postulacion_celular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='celular',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Ej: +56945216387', max_length=128, region=None, verbose_name='Celular'),
        ),
    ]