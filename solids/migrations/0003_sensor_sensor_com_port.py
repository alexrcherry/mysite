# Generated by Django 4.2.1 on 2023-05-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("solids", "0002_rename_votes_measurement_raw_value_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sensor",
            name="sensor_com_port",
            field=models.CharField(default="COM1", max_length=10),
        ),
    ]
