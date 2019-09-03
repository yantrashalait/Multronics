from .models import Notification, Brand, Cart, WaitList, Category, Type, Favourite

def header_processor(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_seen=False).order_by('-date')[:3]
        favourite = Favourite.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
        waitlist = WaitList.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
        cart = Cart.objects.filter(user=request.user, removed=False).order_by('-date')[:3]
        categories = Category.objects.all()
        brands = Brand.objects.all()
        types = Type.objects.all()
        # notification_count = Notification.objects.filter(user=request.user, is_seen=False).count()
        # favourite = Favourite.objects.filter(user=request.user, removed=False).count()
        # cart_count = Cart.objects.filter(user=request.user, removed=False).count()
        context = {
            'menu_notifications': notifications,
            'menu_brands': brands,
            'header_waitlist': waitlist,
            'header_cart': cart,
            'header_favourites': favourite,
            'menu_categories': categories,
            'menu_types': types,   
        }
    else:
        categories = Category.objects.all()
        brands = Brand.objects.all()
        types = Type.objects.all()
        # notification_count = Notification.objects.filter(user=request.user, is_seen=False).count()
        # favourite = Favourite.objects.filter(user=request.user, removed=False).count()
        # cart_count = Cart.objects.filter(user=request.user, removed=False).count()
        context = {
            'menu_brands': brands,
            'menu_categories': categories,
            'menu_types': types,   
        }
    return context