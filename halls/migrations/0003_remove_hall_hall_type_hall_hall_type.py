# Generated by Django 4.1.8 on 2023-04-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("halls", "0002_remove_halltype_hall_hall_hall_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hall",
            name="hall_type",
        ),
        migrations.AddField(
            model_name="hall",
            name="hall_type",
            field=models.ManyToManyField(related_name="halls", to="halls.halltype"),
        ),
    ]