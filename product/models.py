from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.name + '-' + self.name


class Type(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand.name + '-' + self.brand_type


class Product(models.Model):
    name = models.TextField()
    previous_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    new_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='product_category')
    brand = models.ForeignKey(Brand, verbose_name='Brand', on_delete=models.CASCADE, related_name='product_brand')
    views = models.IntegerField(default=0)
    super_deals = models.BooleanField(default=False, verbose_name='Do you want this item to display in super deals section?')
    offer = models.BooleanField(default=False, verbose_name='Does this item have an offer?')
    availability = models.BooleanField(default=False, name='Is this product available in stock?')

    def __str__(self):
        return self.name 


class ProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='highlights')
    highlight = models.TextField(help_text='Enter the highlight text here')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    title = models.CharField(max_length=100)
    content = models.TextField()


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banners/')


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_seen = models.BooleanField(default=False)


class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='wishlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='wishlist', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)
    removed_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username + ' ' + self.product.name


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)
    removed_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username + ' ' + self.product.name
    

class UserBargain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bargain', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='bargain', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.product.name    


@receiver(post_save, sender=Product)
def product_notify(sender, instance, created, **kwargs):
    # check if the product is made available and user have added it to their wish list
    if instance.availability == True:
        if WishList.objects.filter(product=instance).exists():
            users = WishList.objects.filter(product=instance)
            for item in users:
                Notification.objects.create(
                    user=item.user, 
                    date=datetime.now(), 
                    title='Product Available',
                    description='Product ' + item.product.name + ' is available on stock now.')

    # check if price has reduced
    if instance.new_price < instance.old_price:
        if UserBargain.objects.filter(product=instance).exists():
            users = UserBargain.objects.filter(product=instance)
            for item in users:
                Notification.objects.create(
                        user=item.user, 
                        date=datetime.now(), 
                        title='Price Drop',
                        description='Product ' + item.product.name + ' is now available at ' + instance.new_price)
