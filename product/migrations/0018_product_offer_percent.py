# Generated by Django 2.2.4 on 2019-09-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20190902_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_percent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
