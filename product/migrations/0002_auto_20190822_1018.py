# Generated by Django 2.2.4 on 2019-08-22 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='removed_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
