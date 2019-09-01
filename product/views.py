from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product, Category, Brand, Type, BannerImage, ProductImage, ProductSpecification, Cart
from .forms import CartForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    super_deals = Product.objects.filter(super_deals=True)
    most_viewed = Product.objects.filter(views__gte=10)
    offer = Product.objects.filter(offer=True)
    return render(request, 'product/index.html', {'super_deals': super_deals, 'most_viewed':most_viewed, 'offer':offer})


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'product/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.filter(user_id=self.kwargs.get('pk')).order_by('-date')


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'product/cart.html'
    context_object_name = 'carts'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.filter(removed=False).order_by('-date')
        else:
            return Cart.objects.filter(user_id=self.kwargs.get('pk'), removed=False).order_by('-date')


class WaitListView(LoginRequiredMixin, ListView):
    model = WaitList
    template_name = 'product/wait.html'
    context_object_name = 'waitlists'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return WaitList.objects.filter(removed=False).order_by('-date')
        else:
            return WaitList.objects.filter(user_id=self.kwargs.get('pk'), removed=False).order_by('-date')


class FavouriteListView(LoginRequiredMixin, ListView):
    model = Favourite
    template_name = 'product/fav.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return Favourite.objects.filter(user_id=self.kwargs.get('pk'), removed=False).order_by('-date')

    def post(self, request, *args, **kwargs):
        _id = self.request.POST.get('delete')
        fav = Favourite.objects.get(pk=_id)
        fav.removed=True
        fav.save()
        return render(request, self.template_name, {'favourites': self.get_queryset()})

# mark a notification as seen
def see_notification(request, *args, **kwargs):
    notification = Notification.objects.get(id=kwargs.get('pk'))
    notification.is_seen = True
    notification.save()
    return HttpResponse('notification seen')


class ProductList(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'

    # def get_queryset(self):
    #     return Product.objects.all()

    # def get_context_data(self,**kwargs):
    #     context = super(ProductList,self).get_context_data(**kwargs)
    #     return context
      

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product-detail.html'
    context_object_name = 'product'


class AddCart(LoginRequiredMixin, CreateView):
    template_name = 'product/add_cart.html'
    form_class = CartForm

    def get_success_url(self):
        return reverse('product:cart-list', kwargs={'pk':self.request.user.pk})


@login_required(login_url='/login/')
def add_to_favourite(request, *args, **kwargs):
    if request.user.is_authenticated:
        if request.is_ajax():
            _id = request.GET.get('pk')
            product = Product.objects.get(id=_id)
            fav, created = Favourite.objects.get_or_create(product=product, user=request.user)
            if not created:
                if fav.removed == True:
                    fav.removed = False
                    fav.save()
            data = {'pk': _id}
            return HttpResponse(data)
        else:
            return HttpResponse({'message': 'Added Failed'})
    else:
        return HttpResponseRedirect('login')


def brand_list(request, *args, **kwargs):
    brand = Product.objects.filter(brand_id=kwargs.get('pk'))
    return render(request, 'product/product-list.html', {'product':brand})

def type_list(request, *args, **kwargs):
    type = Product.objects.filter(product_type_id=kwargs.get('pk'))
    return render(request, 'product/product-list.html', {'product':type})

def super_deals_list(request, *args, **kwargs):
    super_deals = Product.objects.filter(super_deals=True)
    return render(request, 'product/product-list.html', {'product':super_deals})

def offer_list(request, *args, **kwargs):
    offer = Product.objects.filter(offer=True)
    return render(request, 'product/product-list.html', {'product':offer})

def most_viewed_list(request, *args, **kwargs):
    most_viewed = Product.objects.filter(views__gte=10)
    return render(request, 'product/product-list.html', {'product':most_viewed})

