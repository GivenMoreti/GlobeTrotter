# Generated by Django 4.1.7 on 2023-03-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_trip_date_added_alter_trip_trip_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_name',
        ),
    ]
