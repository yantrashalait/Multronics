from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'previous_price', 'new_price', 'category', 'brand', 'super_deals', 'offer', 'availability']