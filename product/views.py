from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product, Category, Brand, Type, BannerImage
from .forms import ProductForm, CategoryForm, BrandForm, TypeForm, BannerImageForm, CartForm, ProductSpecificationFormset, ProductImageFormset, ProductHighlightFormset
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


# mark a notification as seen
def see_notification(request, *args, **kwargs):
    notification = Notification.objects.get(id=kwargs.get('pk'))
    notification.is_seen = True
    notification.save()
    return HttpResponse('notification seen')


class ProductList(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'product'

    # def get_queryset(self):
    #     return Product.objects.all()

    # def get_context_data(self,**kwargs):
    #     context = super(ProductList,self).get_context_data(**kwargs)
    #     return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class ProductCreate(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['productimage_form'] = ProductImageFormset(self.request.POST)
            context['producthighlight_form'] = ProductHighlightFormset(self.request.POST)
            context['productspecification_form'] = ProductSpecificationFormset(self.request.POST)
        
        else:
            context['productimage_form'] = ProductImageFormset()
            context['producthighlight_form'] = ProductHighlightFormset()
            context['productspecification_form'] = ProductSpecificationFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        productimage_form = context['productimage_form']
        producthighlight_form = context['producthighlight_form']
        productspecification_form = context['productspecification_form']
        if productimage_form.is_valid() and producthighlight_form.is_valid() and productspecification_form.is_valid():
            self.object = form.save()
            productimage_form.instance = self.object
            productimage_form.save()
            producthighlight_form.instance = self.object
            producthighlight_form.save()
            productspecification_form.instance = self.object
            productspecification_form.save()
            return HttpResponseRedirect('/')
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

class CategoryList(ListView):
    template_name = 'product/category_list.html'
    model = Category
    context_object_name = 'category'

class CategoryCreate(CreateView):
    model = Category
    template_name = 'product/category_create.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('product:category-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class CategoryDelete(DeleteView):
    template_name = 'product/category_delete.html'
    form_class = CategoryForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:category-list')

class CategoryUpdate(UpdateView):
    template_name = 'product/category_create.html'
    form_class = CategoryForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:category-list')

class BrandList(ListView):
    template_name = 'product/brand_list.html'
    model = Brand
    context_object_name = 'brand'

class BrandCreate(CreateView):
    model = Brand
    template_name = 'product/brand_create.html'
    form_class = BrandForm

    def get_success_url(self):
        return reverse('product:brand-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BrandDelete(DeleteView):
    template_name = 'product/brand_delete.html'
    form_class = BrandForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:brand-list')

class BrandUpdate(UpdateView):
    template_name = 'product/brand_create.html'
    form_class = BrandForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:brand-list')

class TypeList(ListView):
    template_name = 'product/type_list.html'
    model = Type
    context_object_name = 'type'

class TypeCreate(CreateView):
    model = Type
    template_name = 'product/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('product:type-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TypeDelete(DeleteView):
    template_name = 'product/type_delete.html'
    form_class = TypeForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:type-list')

class TypeUpdate(UpdateView):
    ctemplate_name = 'product/type_create.html'
    form_class = TypeForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:type-list')

class BannerList(ListView):
    template_name = 'product/banner_list.html'
    model = BannerImage
    context_object_name = 'banner'

class BannerCreate(CreateView):
    model = BannerImage
    template_name = 'product/banner_create.html'
    form_class = BannerImageForm

    def get_success_url(self):
        return reverse('product:banner-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BannerDelete(DeleteView):
    template_name = 'product/banner_delete.html'
    form_class = BannerImageForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:banner-list')

class BannerUpdate(UpdateView):
    template_name = 'product/banner_create.html'
    form_class = BannerImageForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:banner-list')


class AddCart(CreateView):
    template_name = 'product/add_cart.html'
    form_class = CartForm

    def get_success_url(self):
        return 

