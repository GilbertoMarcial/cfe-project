# Generated by Django 5.0.1 on 2024-02-02 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0006_alter_equipo_unidades_alter_unidad_equipos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='unidades',
        ),
        migrations.RemoveField(
            model_name='unidad',
            name='equipos',
        ),
        migrations.RemoveField(
            model_name='unidad',
            name='central',
        ),
        migrations.DeleteModel(
            name='Trafo',
        ),
        migrations.DeleteModel(
            name='Equipo',
        ),
        migrations.DeleteModel(
            name='Unidad',
        ),
    ]
