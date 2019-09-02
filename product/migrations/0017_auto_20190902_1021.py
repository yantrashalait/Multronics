# Generated by Django 2.2.4 on 2019-09-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_merge_20190902_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_small_image',
            field=models.ImageField(blank=True, help_text='Image size: width=150px, height=150px', null=True, upload_to='brands/small/'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, help_text='Image Size: width=410px, height=281px', null=True, upload_to='category/'),
        ),
        migrations.AddField(
            model_name='type',
            name='type_image',
            field=models.ImageField(blank=True, help_text='Image size: width=150px, height=150px', null=True, upload_to='type/small/'),
        ),
    ]
