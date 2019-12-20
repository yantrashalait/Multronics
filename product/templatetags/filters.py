from django.template import Library
from product.models import Favourite, WaitList, UserBargain
register = Library()


@register.filter
def check_favourite(obj, pk):
    if Favourite.objects.filter(product=obj, user_id=pk, removed=False).exists():
        return True
    else:
        return False


@register.filter
def check_waitlist(obj, pk):
    if WaitList.objects.filter(product=obj, user_id=pk, removed=False).exists():
        return True
    else:
        return False

@register.filter
def check_bargain(obj, pk):
    if UserBargain.objects.filter(product=obj, user_id=pk).exists():
        return True
    else:
        return False

@register.filter
def space_to_underscore(obj):
    return obj.replace(" ", "_")