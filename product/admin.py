from django.contrib import admin
from .models import Category, Brand, Product, BannerImage, ProductImage, Subscription
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(BannerImage)
admin.site.register(ProductImage)
admin.site.register(Subscription)
