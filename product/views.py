from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    return render(request, 'core/index.html')


def view_notifications(request, *args, **kwargs):
    notifications = Notification.objects.filter(user_id=kwargs.get('pk'))
    if notifications:
        return HttpResponse('notifications found')
    else:
        return HttpResponse('No notifications')


def view_cart(request, *args, **kwargs):
    cart = Cart.objects.filter(user_id=kwargs.get('pk'))
    if cart:
        return HttpResponse('cart found')
    else:
        return HttpResponse('no cart found')


def view_wishlist(request, *args, **kwargs):
    wishlist = WishList.objects.filter(user_id=kwargs.get('pk'))
    if wishlist:
        return HttpResponse('wishlist found')
    else:
        return HttpResponse('no wishlist')


class ProductList(ListView):
    pass


class ProductAdd(CreateView):
    pass


def see_notification(request, *args, **kwargs):
    notification = Notification.objects.get(id=kwargs.get('pk'))
    notification.is_seen = True
    notification.save()
    return HttpResponse('notification seen')