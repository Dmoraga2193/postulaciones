# Generated by Django 4.1.3 on 2023-06-11 18:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_carrito'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carrito',
            new_name='Cart',
        ),
    ]
