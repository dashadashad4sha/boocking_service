# Generated by Django 4.1.8 on 2023-04-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_alter_orderhistory_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderhistory",
            name="end_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="start_date",
            field=models.DateTimeField(null=True),
        ),
    ]