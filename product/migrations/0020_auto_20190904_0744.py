# Generated by Django 2.2.4 on 2019-09-04 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190904_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userorder',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]