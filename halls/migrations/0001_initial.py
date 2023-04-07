# Generated by Django 4.2 on 2023-04-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HallType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('descriptions', models.TextField()),
                ('address', models.TextField()),
                ('capacity', models.IntegerField()),
                ('area', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('views_count', models.IntegerField(default=0)),
                ('type', models.ManyToManyField(related_name='hall_types', to='halls.halltype')),
            ],
        ),
    ]
