# Generated by Django 5.0.1 on 2024-02-08 22:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0023_trafo_enfriamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafo',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pruebas.marca', verbose_name='Marca'),
            preserve_default=False,
        ),
    ]
