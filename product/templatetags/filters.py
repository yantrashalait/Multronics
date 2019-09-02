from django.template import Library
from product.models import Favourite, WaitList
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
