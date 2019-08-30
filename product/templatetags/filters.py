from django.template import Library
from product.models import Favourite
register = Library()


@register.filter
def check_favourite(obj, pk):
    if Favourite.objects.filter(product=obj, user_id=pk, removed=False).exists():
        return True
    else:
        return False
