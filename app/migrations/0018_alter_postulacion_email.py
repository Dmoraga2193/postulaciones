# Generated by Django 4.1.3 on 2023-06-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_postulacion_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='email',
            field=models.EmailField(help_text='Ejemplo: arteplastica@dominio.cl', max_length=254, verbose_name='Correo Electronico'),
        ),
    ]
