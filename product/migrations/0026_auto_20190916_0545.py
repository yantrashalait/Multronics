# Generated by Django 2.2.4 on 2019-09-16 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20190916_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
