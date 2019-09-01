from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product, Category, Brand, Type, BannerImage, ProductImage, ProductSpecification, Cart
from .forms import ProductForm, CategoryForm, BrandForm, TypeForm, BannerImageForm, CartForm, ProductSpecificationFormset, ProductImageFormset
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
    
    def post(self, request, *args, **kwargs):
        _id = self.request.POST.get('delete')
        cart = Cart.objects.get(pk=_id)
        cart.removed=True 
        cart.save()
        return render(request, self.template_name, {'carts': self.get_queryset()})


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


class ProductCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('add_product')
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProductCreate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['imageform'] = ProductImageFormset(self.request.POST, self.request.FILES, prefix='imageform')
            context['specificationform'] = ProductSpecificationFormset(self.request.POST, self.request.FILES, prefix='specform')
        
        else:
            context['imageform'] = ProductImageFormset(prefix='imageform')
            context['specificationform'] = ProductSpecificationFormset(prefix='specform')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        imageform = context['imageform']
        specificationform = context['specificationform']
        if imageform.is_valid() and specificationform.is_valid():
            self.object = form.save()
            for form in imageform:
                f = form.save(commit=False)
                f.product = self.object
                f.save()
            for form in specificationform:
                f = form.save(commit=False)
                f.product = self.object
                f.save()
            return HttpResponseRedirect('/')
        return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_product'
    template_name = 'product/product_create.html'
    form_class = ProductForm
    is_update_view = True

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductUpdate, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['imageform'] = ProductImageFormset(self.request.POST, self.request.FILES, prefix='imageform', instance=self.object)
            context['specificationform'] = ProductSpecificationFormset(self.request.POST, self.request.FILES, prefix='specform', instance=self.object)
        
        else:
            context['imageform'] = ProductImageFormset(instance=self.object, prefix='imageform')
            context['specificationform'] = ProductSpecificationFormset(instance=self.object, prefix='specform')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        imageform = context['imageform']
        specificationform = context['specificationform']
        self.object = form.save()
        if imageform.is_valid() and specificationform.is_valid():
            for form in imageform:
                f = form.save(commit=False)
                f.product = self.object
                f.save()
            for form in specificationform:
                f = form.save(commit=False)
                f.product = self.object
                f.save()
            return HttpResponseRedirect('/')
        return super().form_valid(form)


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_product'
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

class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'add_category'
    model = Category
    template_name = 'product/category_create.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('product:category-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class CategoryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_category'
    template_name = 'product/category_delete.html'
    form_class = CategoryForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:category-list')

class CategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_category'
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

class BrandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'add_brand'
    model = Brand
    template_name = 'product/brand_create.html'
    form_class = BrandForm

    def get_success_url(self):
        return reverse('product:brand-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BrandDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_brand'
    template_name = 'product/brand_delete.html'
    form_class = BrandForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:brand-list')

class BrandUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_brand'
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

class TypeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'add_type'
    model = Type
    template_name = 'product/type_create.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('product:type-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TypeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_type'
    template_name = 'product/type_delete.html'
    form_class = TypeForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:type-list')

class TypeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_type'
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

class BannerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'add_bannerimage'
    model = BannerImage
    template_name = 'product/banner_create.html'
    form_class = BannerImageForm

    def get_success_url(self):
        return reverse('product:banner-list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class BannerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_bannerimage'
    template_name = 'product/banner_delete.html'
    form_class = BannerImageForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)
    
    def get_success_url(self):
        return reverse('product:banner-list')

class BannerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_bannerimage'
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


class AddCart(LoginRequiredMixin, CreateView):
    form_class = CartForm

    def post(self, request, *args, **kwargs):
        color = request.POST.get("color")
        quantity = request.POST.get("quantity")
        product_id = request.POST.get("product")
        product = Product.objects.get(id=int(product_id))
        cart = Cart()
        cart.color=color
        cart.amount=quantity
        cart.user=request.user
        cart.product=product
        cart.save()
        return HttpResponseRedirect(reverse('product:cart-list', kwargs={'pk': request.user.pk}))

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

