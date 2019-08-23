from .models import Notification, Brand, Cart, Wishlist

def header_processor(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-date')
    brands = Brand.objects.all()
    notification_count = Notification.objects.filter(user=request.user, is_seen=False).count()
    wishlist_count = Wishlist.objects.filter(user=request.user, removed=False).count()
    cart_count = Cart.objects.filter(user=request.user, removed=False).count()
    context = {
        'notifications': notifications,
        'brands': brands,
        'notification_count': notification_count,
        'wishlist_count': wishlist_count,
        'cart_count': cart_count
    }

    return HttpResponse('notifications')