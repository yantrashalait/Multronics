from django.contrib import admin
from .models import Category, Brand, Type, Product, BannerImage
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(BannerImage)
