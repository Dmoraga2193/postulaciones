# Generated by Django 4.1.3 on 2023-06-10 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_alter_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('region', models.CharField(choices=[('Región de Arica y Parinacota', 'Región de Arica y Parinacota'), ('Región de Tarapacá', 'Región de Tarapacá'), ('Región de Antofagasta', 'Región de Antofagasta'), ('Región de Atacama', 'Región de Atacama'), ('Región de Coquimbo', 'Región de Coquimbo'), ('Región de Valparaíso', 'Región de Valparaíso'), ('Región Metropolitana', 'Región Metropolitana'), ("Región de O'Higgins", "Región de O'Higgins"), ('Región del Maule', 'Región del Maule'), ('Región del Ñuble', 'Región del Ñuble'), ('Región del Biobío', 'Región del Biobío'), ('Región de La Araucanía', 'Región de La Araucanía'), ('Región de Los Ríos', 'Región de Los Ríos'), ('Región de Los Lagos', 'Región de Los Lagos'), ('Región de Aysén', 'Región de Aysén'), ('Región de Magallanes', 'Región de Magallanes')], max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None)),
                ('codigo_postal', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
