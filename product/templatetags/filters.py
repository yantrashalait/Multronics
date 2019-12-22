from django.template import Library
from product.models import Favourite, WaitList, UserBargain, Product
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


@register.filter
def separate_two(popular):
    total = len(popular)
    if total < 2:
        return range(1)
    else:
        if(total / 2) == 0:
            return range((total / 2))
        else:
            return range((total // 2) + 1)


@register.filter
def block_viewed(popular, index=None):
    if index == 1:
        return Product.objects.filter(views__gte=10, visibility=True)[:2]

    if index > 1:
        start = (index - 1) * 2
        end = start + 2
        return Product.objects.filter(views__gte=10, visibility=True)[start:end]

