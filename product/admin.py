from django.contrib import admin
from .models import Category, Brand, Type, Product, BannerImage, ProductImage, Cart, Subscription
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(BannerImage)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(Subscription)