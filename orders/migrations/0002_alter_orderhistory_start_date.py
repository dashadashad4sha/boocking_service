# Generated by Django 4.1.8 on 2023-05-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderhistory",
            name="start_date",
            field=models.DateTimeField(null=True),
        ),
    ]