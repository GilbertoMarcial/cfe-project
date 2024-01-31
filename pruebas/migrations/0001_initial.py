# Generated by Django 5.0.1 on 2024-01-31 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
            ],
            options={
                'verbose_name': 'EPS',
                'verbose_name_plural': 'EPS',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subgerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modify', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('eps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.eps', verbose_name='EPS')),
            ],
            options={
                'verbose_name': 'Subgerencia',
                'verbose_name_plural': 'Subgerencias',
                'ordering': ['name'],
            },
        ),
    ]