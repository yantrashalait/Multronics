from product.models import AboutITeam, UserOrder, UserRequestProduct

def base_processor(request):
    if request.user.is_authenticated:
        about = AboutITeam.objects.last()
        orders = UserOrder.objects.all().order_by('date')[:3]
        requested_products = UserRequestProduct.objects.all().order_by('date')[:3]
        return {'about': about, 'orders': orders, 'requested_products': requested_products}
    else:
        return {}
