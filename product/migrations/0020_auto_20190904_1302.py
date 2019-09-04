# Generated by Django 2.2.4 on 2019-09-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20190904_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequestproduct',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userrequestproduct',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userrequestproduct',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userrequestproduct',
            name='product_type',
            field=models.CharField(blank=True, help_text='e.g., Laptop, Desktop', max_length=100, null=True),
        ),
    ]
