# Generated by Django 4.2.16 on 2024-11-30 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_favoriteword_learning_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteword',
            name='learning_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 30, 14, 55, 20, 753109, tzinfo=datetime.timezone.utc)),
        ),
    ]