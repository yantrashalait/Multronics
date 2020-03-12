from django.template import Library
from product.models import Product
register = Library()


@register.filter
def space_to_underscore(obj):
    return obj.replace(" ", "_")


@register.filter
def separate_two(popular):
    total = len(popular)
    if total < 2:
        return range(2)
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


@register.filter
def block_category(category, index=None):
    if index == 1:
        return Product.objects.filter(visibility=True, category=category)[:2]

    if index > 1:
        start = (index - 1) * 2
        end = start + 2
        return Product.objects.filter(visibility=True, category=category)[start:end]
