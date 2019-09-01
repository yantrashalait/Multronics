from django import forms
from product.models import Product, Category, Brand, Type, BannerImage, Cart, ProductSpecification, ProductImage
from django.forms.models import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'description', 'previous_price', 'new_price', 'category', 'brand', 'product_type', 'super_deals', 'offer', 'availability', 'main_image']


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


class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['title', 'content']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['big_image', 'thumbnail_image']


ProductImageFormset = inlineformset_factory(Product, ProductImage, form=ProductImageForm, fields=['big_image', 'thumbnail_image'], extra=1, max_num=10)
ProductSpecificationFormset = inlineformset_factory(Product, ProductSpecification, form=ProductSpecificationForm, fields=['title', 'content'], extra=1, max_num=20)