# Generated by Django 5.0.1 on 2024-02-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0025_trafo_estatus_revision_trafo_fecha_revision_aprobada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafo',
            name='estatus_revision',
            field=models.CharField(choices=[('1', 'Aprobada'), ('2', 'Pendiente')], default='2', verbose_name='Estatus de Revisión'),
        ),
    ]