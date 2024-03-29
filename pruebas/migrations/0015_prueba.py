# Generated by Django 5.0.1 on 2024-02-06 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0014_remove_electricatrafo_prueba_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=50, unique=True, verbose_name='Matrícula')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('trafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.trafo', verbose_name='Trafo')),
            ],
            options={
                'verbose_name': 'Prueba',
                'verbose_name_plural': 'Pruebas',
                'ordering': ['matricula'],
            },
        ),
    ]
