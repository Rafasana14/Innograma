# Generated by Django 4.1.2 on 2022-11-22 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_evento_aforo_max_alter_evento_n_asistentes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evento",
            name="coste",
            field=models.FloatField(
                blank=True,
                default=None,
                null=True,
                validators=[django.core.validators.MinValueValidator(0.0)],
            ),
        ),
    ]