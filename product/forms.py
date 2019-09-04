from django import forms
from .models import Cart, UserRequestProduct
from django.forms.models import inlineformset_factory





class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'amount', 'color']

class UserRequestProductForm(forms.ModelForm):
    class Meta:
        model = UserRequestProduct
        fields = ['product_name', 'type', 'specification', 'contact_number', 'email', 'name', 'amount' ]