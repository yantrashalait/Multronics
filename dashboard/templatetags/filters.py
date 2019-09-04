from django.template import Library
from product.models import Cart, WaitList, UserBargain
register = Library()


@register.filter
def get_cart(obj):
    return Cart.objects.filter(orders=obj, removed=False)