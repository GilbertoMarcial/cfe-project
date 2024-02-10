# Generated by Django 5.0.1 on 2024-02-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0024_trafo_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafo',
            name='estatus_revision',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estatus de Revisión'),
        ),
        migrations.AddField(
            model_name='trafo',
            name='fecha_revision_aprobada',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Revisión Aprobada'),
        ),
    ]
