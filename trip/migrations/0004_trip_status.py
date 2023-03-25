# Generated by Django 4.1.7 on 2023-03-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_alter_trip_trip_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Requested', 'Requested'), ('Completed', 'Completed')], default='Active', max_length=30),
        ),
    ]
