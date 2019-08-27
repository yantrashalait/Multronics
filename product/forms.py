from django import forms
from .models import Product, Category, Brand, Type, BannerImage, Cart, ProductHighlight, ProductSpecification, ProductImage
from django.forms.models import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'previous_price', 'new_price', 'category', 'brand', 'super_deals', 'offer', 'availability']

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


class ProductHighlightForm(forms.ModelForm):
    class Meta:
        model = ProductHighlight
        fields = '__all__'


class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = '__all__'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'


ProductHighlightFormset = inlineformset_factory(
    Product, ProductHighlight, 
    form=ProductHighlightForm,
    fields = ['highlight'],
    extra=2,
    can_delete=True)


ProductSpecificationFormset = inlineformset_factory(
    Product, ProductSpecification, 
    form=ProductSpecificationForm,
    fields = ['title', 'content'],
    extra=2,
    can_delete=True)


ProductImageFormset = inlineformset_factory(
    Product, ProductImage, 
    form=ProductImageForm,
    fields = ['image'],
    extra=2,
    can_delete=True)