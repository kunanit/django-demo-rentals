# Generated by Django 2.2 on 2019-04-04 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('vehicle', models.CharField(max_length=200)),
                ('start_x', models.FloatField()),
                ('start_y', models.FloatField()),
                ('end_x', models.FloatField()),
                ('end_y', models.FloatField()),
            ],
        ),
    ]
