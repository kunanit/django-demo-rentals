# Generated by Django 2.2 on 2019-04-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20190411_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_x',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_y',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
