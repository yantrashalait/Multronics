from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.urls import reverse
from django.core.mail import send_mail


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category/', null=True, blank=True, help_text='Image Size: width=410px, height=281px')

    def __str__(self):
        return self.name


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=100)
    brand_image = models.ImageField(upload_to='brands/', null=True, blank=True, help_text="Image size: width=193px height=115px")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    previous_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    new_price = models.CharField(max_length=100, help_text=('e.g., Rs. 150000'), null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='product_category')
    brand = models.ForeignKey(Brand, verbose_name='Brand', on_delete=models.CASCADE, related_name='product_brand')
    views = models.IntegerField(default=0)
    super_deals = models.BooleanField(default=False, verbose_name='Do you want this item to display in super deals section?')
    offer = models.BooleanField(default=False, verbose_name='Does you want this item to be displayed in offer section?')
    availability = models.BooleanField(default=True, verbose_name='Is this product available in stock?')
    main_image = models.ImageField(upload_to='products/', null=True, blank=True, help_text="Image size: width=265px height=290px")
    offer_tag = models.CharField(max_length=100, null=True, blank=True, help_text="E.g. 15% off")
    visibility = models.BooleanField(default=True, verbose_name="Make this product visibile?")

    def __str__(self):
        return self.name

    def save(self):
        if self.previous_price and self.previous_price > self.new_price:
            offer = round(((int(self.previous_price) - int(self.new_price)) / int(self.previous_price)), 2)* 100
            self.offer_tag = offer
        super(Product, self).save()



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    big_image = models.ImageField(upload_to='products/big/', null=True, blank=True, help_text="Image size: width=700 px height=700px")
    thumbnail_image = models.ImageField(upload_to='products/thumbnail/', null=True, blank=True, help_text="Image size: width=100px height=100px")


class BannerImage(models.Model):
    image = models.ImageField(upload_to='banners/', help_text="Image size: width=1280px height=435px")


class Subscription(models.Model):
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

    def __str__(self):
        return self.email


class SpecificationTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SpecificationContent(models.Model):
    title = models.ForeignKey(SpecificationTitle, on_delete=models.CASCADE, related_name="content")
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    title = models.ForeignKey(SpecificationTitle, on_delete=models.CASCADE, related_name="product_title")
    content = models.ForeignKey(SpecificationContent, on_delete=models.CASCADE, related_name="product_content")


class AboutITeam(models.Model):
    contact1 = models.CharField(max_length=100, default='')
    contact2 = models.CharField(max_length=100, null=True, blank=True)
    contact3 = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo/", help_text="Image size: width=192px height=31px")
    address = models.CharField(max_length=255, null=True, blank=True)
    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    youtube_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email
