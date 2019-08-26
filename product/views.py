from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product 
from .forms import ProductForm
from django.urls import reverse


def index(request):
    return render(request, 'product/index.html')


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

# def product_detail_view(request):

    # obj = Product.objects.all()
    # context = {
    #     'name': obj.name,
    #     # 'previous_price': obj.previous_price,
    #     # 'new_price': obj.new_price
    # }
    # return render(request, "product/product_detail.html", {'object': obj})

class ProductList(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'product'

    # def get_queryset(self):
    #     return Product.objects.all()

    # def get_context_data(self,**kwargs):
    #     context = super(ProductList,self).get_context_data(**kwargs)
    #     return context

# class ProductAdd(CreateView):
#     template_name = 'product/product_add.html'
#     model = Product
#     context_object_name = 'product'
      

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    

# def product_add(request):
#     model = Product
#     return render(request, 'product/product_add.html')


def see_notification(request, *args, **kwargs):
    notification = Notification.objects.get(id=kwargs.get('pk'))
    notification.is_seen = True
    notification.save()
    return HttpResponse('notification seen')


class ProductCreate(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductUpdate(UpdateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDelete(DeleteView):
    template_name = 'product/product_delete.html'
    form_class = ProductForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:product-list')

  