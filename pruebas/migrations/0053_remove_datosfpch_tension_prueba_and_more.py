# Generated by Django 5.0.1 on 2024-02-19 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0052_datosfpcht_datosfpct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosfpch',
            name='tension_prueba',
        ),
        migrations.RemoveField(
            model_name='datosfpchl',
            name='tension_prueba',
        ),
        migrations.RemoveField(
            model_name='datosfpcht',
            name='tension_prueba',
        ),
        migrations.RemoveField(
            model_name='datosfpct',
            name='tension_prueba',
        ),
        migrations.RemoveField(
            model_name='datosfpcl',
            name='tension_prueba',
        ),
        migrations.RemoveField(
            model_name='datosfpch',
            name='electrica_trafo',
        ),
        migrations.RemoveField(
            model_name='datosfpchl',
            name='electrica_trafo',
        ),
        migrations.RemoveField(
            model_name='datosfpcht',
            name='electrica_trafo',
        ),
        migrations.RemoveField(
            model_name='datosfpcl',
            name='electrica_trafo',
        ),
        migrations.RemoveField(
            model_name='datosfpct',
            name='electrica_trafo',
        ),
        migrations.DeleteModel(
            name='DatosFP',
        ),
        migrations.DeleteModel(
            name='DatosFPCH',
        ),
        migrations.DeleteModel(
            name='DatosFPCHL',
        ),
        migrations.DeleteModel(
            name='DatosFPCHT',
        ),
        migrations.DeleteModel(
            name='DatosFPCL',
        ),
        migrations.DeleteModel(
            name='DatosFPCT',
        ),
    ]