# Generated by Django 4.1.7 on 2023-03-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_alter_trip_trip_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='seats_avail',
            field=models.IntegerField(default=None),
        ),
    ]