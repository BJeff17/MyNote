# Generated by Django 5.0.4 on 2024-04-15 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_note_date_alter_note_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='score',
            field=models.IntegerField(choices=[(1, 'plutot inutile'), (2, 'pas si utile'), (3, 'assez utile'), (4, 'Utile'), (5, 'tres utile')], default=3),
        ),
        migrations.AlterField(
            model_name='note',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 7, 14, 19, 677316)),
        ),
    ]
