from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    return render(request, 'core/index.html')


# class NotificationList(ListView):
#     model = Notification
#     template_name = 'product/notification_list.html'
#     context_object_name = 'notifications'

#     def get_queryset(self, *args, **kwargs):
#         return self.queryset.filter(user_id=kwargs.get('pk')).order_by('-date')

def view_notifications(request, *args, **kwargs):
    notifications = Notification.objects.filter(user_id=kwargs.get('pk')).order_by('-date')
    if notifications:
        return HttpResponse('notifications found')
    else:
        return HttpResponse('No notifications')


# class CartList(ListView):
#     model = Cart
#     template_name = 'product/cart_list.html'
#     context_object_name = 'carts'

#     def get_queryset(self, *args, **kwargs):
#     def get_queryset(self, *args, **kwargs):
#         if self.request.user.is_superuser():
#             return self.queryset.filter(removed=False).order_by('-date')
#         else:
#             return self.queryset.filter(user_id=kwargs.get('pk'), removed=False).order_by('-date')


def view_cart(request, *args, **kwargs):
    if request.user.is_superuser():
        cart = Cart.objects.filter(removed=False).order_by('-date')
    else:
        cart = Cart.objects.filter(user_id=kwargs.get('pk'), removed=False).order_by('date')
    if cart:
        return HttpResponse('cart found')
    else:
        return HttpResponse('no cart found')


# class WaitListView(ListView):
#     model = WaitList
#     template_name = 'product/wait_list.html'
#     context_object_name = 'waitlists'

#     def get_queryset(self, *args, **kwargs):
#         if self.request.user.is_superuser():
#             return self.queryset.filter(removed=False).order_by('-date')
#         else:
#             return self.queryset.filter(user_id=kwargs.get('pk'), removed=False).order_by('-date')


def view_waitlist(request, *args, **kwargs):
    if request.user.is_superuser():
        waitlist = WaitList.objects.filter(removed=False).order_by('-date')
    else:
        waitlist = WaitList.objects.filter(user_id=kwargs.get('pk'), removed=False).order_by('-date')
    if wishlist:
        return HttpResponse('waitlist found')
    else:
        return HttpResponse('no waitlist')


# class FavouriteList(ListView):
#     model = Favourite
#     template_name = 'product/favourite_list.html'
#     context_object_name = 'favourites'

#     def get_queryset(self, *args, **kwargs):
#         return self.queryset.filter(user_id=kwargs.get('pk'), removed=False).order_by('-date')


def view_favourite(request, *args, **kwargs):
    favourite = Favourite.objects.filter(user_id=kwargs.get('pk'), removed=False).order_by('-date')
    if favourite:
        return HttpResponse('favourite found')
    else:
        return HttpResponse('favourite not found')


class ProductList(ListView):
    pass


class ProductAdd(CreateView):
    pass


def see_notification(request, *args, **kwargs):
    notification = Notification.objects.get(id=kwargs.get('pk'))
    notification.is_seen = True
    notification.save()
    return HttpResponse('notification seen')