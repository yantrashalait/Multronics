from django.template import Library
from product.models import Cart, WaitList, UserBargain
register = Library()


@register.filter
def get_cart(obj):
    print(Cart.objects.filter(orders=obj, removed=False))
    return Cart.objects.filter(orders=obj, removed=False)