from django import forms
from .models import Product, Category, Brand, Type, BannerImage


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