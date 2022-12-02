# Generated by Django 4.1.2 on 2022-11-29 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_remove_ponente_conferencias_impartidas_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="conferencia", name="ponente",),
        migrations.CreateModel(
            name="Ponente_Conferencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "conferencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.conferencia",
                    ),
                ),
                (
                    "ponente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ponente"
                    ),
                ),
            ],
        ),
    ]
