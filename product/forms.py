from django import forms
from .models import Cart, UserRequestProduct, UserOrder
from django.forms.models import inlineformset_factory


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'amount', 'color']

class UserRequestProductForm(forms.ModelForm):
    class Meta:
        model = UserRequestProduct
        fields = ['product_name', 'product_type', 'specification', 'contact_number', 'email', 'name', 'amount' ]

class UserOrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = "__all__"