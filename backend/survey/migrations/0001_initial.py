# Generated by Django 4.2.3 on 2023-07-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
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
                ("sruvey_name", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
        ),
    ]
