# Generated by Django 2.2.4 on 2019-08-23 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190822_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='removed_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
