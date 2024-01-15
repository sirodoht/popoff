# Generated by Django 5.0.1 on 2024-01-15 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_entry_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matching",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="content_entry",
                        to="main.entry",
                    ),
                ),
                (
                    "informed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="informed_entry",
                        to="main.entry",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="entry",
            name="knows_about",
            field=models.ManyToManyField(through="main.Matching", to="main.entry"),
        ),
    ]
