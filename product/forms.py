from django import forms
from .models import Cart, UserOrder
from django.forms.models import inlineformset_factory


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'amount', 'color']


class UserOrderForm(forms.ModelForm):
    class Meta:
        model = UserOrder
        fields = "__all__"