# Generated by Django 5.0.4 on 2024-04-14 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 18, 26, 50, 23117)),
        ),
    ]
