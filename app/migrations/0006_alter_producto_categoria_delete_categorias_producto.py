# Generated by Django 4.1.3 on 2023-06-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_categorias_producto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[('AC', 'Acelerante'), ('AD', 'Aditivo'), ('CT', 'Catalizador'), ('CA', 'Carga'), ('EP', 'Epóxico'), ('FV', 'Fibra de vidrio'), ('GC', 'Gel Coat'), ('PO', 'Poliuretano'), ('RE', 'Resina'), ('SV', 'solvente')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Categorias_producto',
        ),
    ]
