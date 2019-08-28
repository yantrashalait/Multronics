from django import forms
from .models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, ProductImage
from django.forms import formset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'availability']

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
        fields = ['image',]


ProductImageFormset = formset_factory(ProductImageForm, extra=1, max_num=10)
ProductSpecificationFormset = formset_factory(ProductSpecificationForm, extra=1, max_num=20)