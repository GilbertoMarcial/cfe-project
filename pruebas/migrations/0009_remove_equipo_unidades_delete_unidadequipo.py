# Generated by Django 5.0.1 on 2024-02-05 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0008_equipo_trafo_unidad_unidadequipo_equipo_unidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='unidades',
        ),
        migrations.DeleteModel(
            name='UnidadEquipo',
        ),
    ]
