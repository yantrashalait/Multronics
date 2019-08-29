from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=100)
    brand_image = models.ImageField(upload_to='brands/', null=True, blank=True, help_text="Image size: width=193px height=115px")

    def __str__(self):
        return self.category.name + '-' + self.name


class Type(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand.name + '-' + self.brand_type


class Product(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    previous_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    new_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='product_category')
    brand = models.ForeignKey(Brand, verbose_name='Brand', on_delete=models.CASCADE, related_name='product_brand')
    product_type = models.ForeignKey(Type, verbose_name='Type of laptop', on_delete=models.CASCADE, related_name='product_type', null=True, blank=True)
    views = models.IntegerField(default=0)
    super_deals = models.BooleanField(default=False, verbose_name='Do you want this item to display in super deals section?')
    offer = models.BooleanField(default=False, verbose_name='Does this item have an offer?')
    availability = models.BooleanField(default=False, verbose_name='Is this product available in stock?')
    main_image = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Image size: width=265px height=290px")

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("product:product-list")


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    big_image = models.ImageField(upload_to='products/big/', null=True, blank=True, help_text="Image size: width=700 px height=700px")
    thumbnail_image = models.ImageField(upload_to='products/thumbnail/', null=True, blank=True, help_text="Image size: width=100px height=100px")


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    title = models.CharField(max_length=100)
    content = models.TextField()


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banners/', help_text="Image size: width=193px height=115px")


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notification', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_seen = models.BooleanField(default=False)


class WaitList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='waitlist', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='waitlist', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)
    removed_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username + ' ' + self.product.name


class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='favourite', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favourite', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' ' + self.product.name


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart', on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
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


class UserRequestProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_request', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    specification = models.TextField()
    active = models.BooleanField(default=False)
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ' ' + self.product_name



@receiver(post_save, sender=Product)
def product_notify(sender, instance, created, **kwargs):
    # check if the product is made available and user have added it to their wish list
    if instance.availability == True:
        if WaitList.objects.filter(product=instance).exists():
            users = WaitList.objects.filter(product=instance)
            for item in users:
                Notification.objects.create(
                    user=item.user, 
                    date=datetime.now(), 
                    title='Product Available',
                    description='Product ' + item.product.name + ' is available on stock now.')

    # check if price has reduced
    if instance.new_price < instance.previous_price:
        if UserBargain.objects.filter(product=instance).exists():
            users = UserBargain.objects.filter(product=instance)
            for item in users:
                Notification.objects.create(
                        user=item.user, 
                        date=datetime.now(), 
                        title='Price Drop',
                        description='Product ' + item.product.name + ' is now available at ' + instance.new_price)
