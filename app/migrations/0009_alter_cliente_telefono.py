# Generated by Django 4.1.3 on 2023-06-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]
