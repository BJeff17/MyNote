# Generated by Django 5.0.4 on 2024-04-11 20:39

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('score', models.IntegerField(choices=[(1, 'plutot inutile'), (2, 'pas si utile'), (3, 'assez utile'), (4, 'Utiile'), (5, 'tres utile')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('status', models.BooleanField(choices=[(True, 'actif'), (False, 'expiré')], default=True)),
                ('expiration', models.DateTimeField(default=datetime.datetime(2024, 4, 21, 21, 39, 37, 833898))),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categorie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
