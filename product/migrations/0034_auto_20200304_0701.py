# Generated by Django 2.2.6 on 2020-03-04 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20200301_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='product',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='product',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='OfferImage',
        ),
        migrations.DeleteModel(
            name='SuperImage',
        ),
        migrations.RemoveField(
            model_name='userbargain',
            name='product',
        ),
        migrations.RemoveField(
            model_name='userbargain',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserRequestProduct',
        ),
        migrations.RemoveField(
            model_name='waitlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='waitlist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='UserBargain',
        ),
        migrations.DeleteModel(
            name='UserOrder',
        ),
        migrations.DeleteModel(
            name='WaitList',
        ),
    ]
