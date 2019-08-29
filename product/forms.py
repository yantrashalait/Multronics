from django import forms
from .models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, ProductImage
from django.forms.models import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'availability', 'main_image']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['category', 'name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['brand', 'brand_type']

class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['image']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product', 'amount', 'color']


class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['title', 'content']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['big_image', 'thumbnail_image']


ProductImageFormset = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=1, max_num=10)
ProductSpecificationFormset = inlineformset_factory(Product, ProductSpecification, form=ProductSpecificationForm, extra=1, max_num=20)