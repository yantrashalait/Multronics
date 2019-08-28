from .models import Notification, Brand, Cart, Wishlist, Category, Type, Waitlist, Favourite

def header_processor(request):
    notifications = Notification.objects.filter(user=request.user, is_seen=False).order_by('-date')[:3]
    favourite = Favourite.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
    waitlist = Waitlist.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
    cart = Cart.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
    categories = Category.objects.all()
    brands = Brand.objects.all()
    types = Type.objects.all()
    notification_count = Notification.objects.filter(user=request.user, is_seen=False).count()
    wishlist_count = Wishlist.objects.filter(user=request.user, removed=False).count()
    cart_count = Cart.objects.filter(user=request.user, removed=False).count()
    context = {
        'notifications': notifications,
        'brands': brands,
        'notification_count': notification_count,
        'wishlist_count': wishlist_count,
        'cart_count': cart_count,
        'header_waitlist': waitlist,
        'header_cart': cart,
        'header_favourites': favourite,
        'categories': categories
    }

    return context