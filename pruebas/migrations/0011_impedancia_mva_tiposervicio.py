# Generated by Django 5.0.1 on 2024-02-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0010_equipo_unidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impedancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('z_1', models.FloatField(default=0, verbose_name='Z 1')),
                ('z_2', models.FloatField(default=0, verbose_name='Z 2')),
                ('z_3', models.FloatField(default=0, verbose_name='Z 3')),
                ('z_4', models.FloatField(default=0, verbose_name='Z 4')),
            ],
            options={
                'verbose_name': 'Impedancia',
                'verbose_name_plural': 'Impedancias',
            },
        ),
        migrations.CreateModel(
            name='MVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mva_1', models.FloatField(default=0, verbose_name='MVA 1')),
                ('mva_2', models.FloatField(default=0, verbose_name='MVA 2')),
                ('mva_3', models.FloatField(default=0, verbose_name='MVA 3')),
                ('mva_4', models.FloatField(default=0, verbose_name='MVA 4')),
            ],
            options={
                'verbose_name': 'MVA',
                'verbose_name_plural': 'MVA',
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Servicio',
                'verbose_name_plural': 'Tipos de Servicio',
                'ordering': ['name'],
            },
        ),
    ]
