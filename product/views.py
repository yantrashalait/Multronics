from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Product, Category, Brand, BannerImage, ProductImage, ProductSpecification, Subscription
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render_to_response('dashboard/404.html')
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render_to_response('dashboard/500.html')
    response.status_code = 500
    return response


def index(request):
    super_deals = Product.objects.filter(super_deals=True, visibility=True)
    most_viewed = Product.objects.filter(views__gte=10, visibility=True)
    offer = Product.objects.filter(offer=True, visibility=True)
    brand = Brand.objects.all()
    banner = BannerImage.objects.all()
    category = Category.objects.all()
    return render(request, 'product/index.html', {'super_deals': super_deals, 'most_viewed':most_viewed, 'offer':offer, 'brand':brand, 'banner': banner, 'category': category})


class ProductList(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 10
    queryset = Product.objects.filter(visibility=True)

    def get_queryset(self, *args, **kwargs):
        brands = self.request.GET.getlist('brands')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        brand_ids = []
        for brand_id in brands:
            brand_ids.append(int(brand_id))
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if brand_ids and min_price and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__range=(min_price, max_price), visibility=True)
        elif brand_ids and min_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__gte=min_price, visibility=True)
        elif brand_ids and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__lte=max_price, visibility=True)
        elif min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), visibility=True)
        elif brand_ids:
            return Product.objects.filter(brand_id__in=brand_ids, visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, visibility=True)
        return Product.objects.filter(visibility=True)

    def get_context_data(self,**kwargs):
        context = super(ProductList,self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product-detail.html'
    context_object_name = 'product'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=id_)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        self.object.views += 1
        self.object.save()
        context['brands'] = Brand.objects.all()
        context['related'] = Product.objects.filter( ~Q(id=self.object.id), category=self.object.category, brand=self.object.brand, visibility=True)[:10]
        return context


class CategoryListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        brands = self.request.GET.getlist('brands')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        brand_ids = []
        for brand_id in brands:
            brand_ids.append(int(brand_id))
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if brand_ids and min_price and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__range=(min_price, max_price), category_id=self.kwargs.get("pk"), visibility=True)
        elif brand_ids and min_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__gte=min_price, category_id=self.kwargs.get("pk"), visibility=True)
        elif brand_ids and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__lte=max_price, category_id=self.kwargs.get("pk"), visibility=True)
        elif min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), category_id=self.kwargs.get("pk"), visibility=True)
        elif brand_ids:
            return Product.objects.filter(brand_id__in=brand_ids, category_id=self.kwargs.get("pk"), visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, category_id=self.kwargs.get("pk"), visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, category_id=self.kwargs.get("pk"), visibility=True)
        return Product.objects.filter(category_id=self.kwargs.get("pk"), visibility=True)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.filter(category_id=self.kwargs.get('pk'))
        return context


class BrandListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), brand_id=self.kwargs.get("pk"), visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, brand_id=self.kwargs.get("pk"), visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, brand_id=self.kwargs.get("pk"),  visibility=True)
        return Product.objects.filter(brand_id=self.kwargs.get("pk"), visibility=True)


class SuperDealsListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        brands = self.request.GET.getlist('brands')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        brand_ids = []
        for brand_id in brands:
            brand_ids.append(int(brand_id))
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if brand_ids and min_price and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__range=(min_price, max_price), super_deals=True, visibility=True)
        elif brand_ids and min_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__gte=min_price, super_deals=True, visibility=True)
        elif brand_ids and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__lte=max_price, super_deals=True, visibility=True)
        elif min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), super_deals=True, visibility=True)
        elif brand_ids:
            return Product.objects.filter(brand_id__in=brand_ids, super_deals=True, visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, super_deals=True, visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, super_deals=True, visibility=True)
        return Product.objects.filter(super_deals=True, visibility=True)

        def get_context_data(self, *args, **kwargs):
            context = super(SuperDealsListView, self).get_context_data(**kwargs)
            context['brands'] = Brand.objects.all()
            return context

class OfferListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        brands = self.request.GET.getlist('brands')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        brand_ids = []
        for brand_id in brands:
            brand_ids.append(int(brand_id))
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if brand_ids and min_price and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__range=(min_price, max_price), offer=True, visibility=True)
        elif brand_ids and min_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__gte=min_price, offer=True, visibility=True)
        elif brand_ids and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__lte=max_price, offer=True, visibility=True)
        elif min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), offer=True, visibility=True)
        elif brand_ids:
            return Product.objects.filter(brand_id__in=brand_ids, offer=True, visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, offer=True, visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, offer=True, visibility=True)
        return Product.objects.filter(offer=True, visibility=True)

    def get_context_data(self, *args, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context


class MostViewedListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'product'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        brands = self.request.GET.getlist('brands')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        brand_ids = []
        for brand_id in brands:
            brand_ids.append(int(brand_id))
        try:
            if min_price.isdigit():
                min_price = int(min_price)
            else:
                min_price = None
        except:
            min_price = None
        try:
            if max_price.isdigit():
                max_price = int(max_price)
            else:
                max_price = None
        except:
            max_price = None

        if brand_ids and min_price and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__range=(min_price, max_price), views__gte=10, visibility=True)
        elif brand_ids and min_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__gte=min_price, views__gte=10, visibility=True)
        elif brand_ids and max_price:
            return Product.objects.filter(brand_id__in=brand_ids, new_price__lte=max_price, views__gte=10, visibility=True)
        elif min_price and max_price:
            return Product.objects.filter(new_price__range=(min_price, max_price), views__gte=10, visibility=True)
        elif brand_ids:
            return Product.objects.filter(brand_id__in=brand_ids, views__gte=10, visibility=True)
        elif min_price:
            return Product.objects.filter(new_price__gte=min_price, views__gte=10, visibility=True)
        elif max_price:
            return Product.objects.filter(new_price__lte=max_price, views__gte=10, visibility=True)
        return Product.objects.filter(views__gte=10, visibility=True)

    def get_context_data(self, *args, **kwargs):
        context = super(MostViewedListView, self).get_context_data(**kwargs)
        context['brands'] = Brands.objects.all()
        return context


def search_product(request):
    if request.method=='POST':
        search = request.POST.get('srh')

        if search:
            match = Product.objects.filter(Q(name__icontains=search) | Q(category__name__icontains=search) | Q(brand__name__icontains=search), visibility=True)

            if match:
                return render(request, 'product/product-list.html', {'product':match, 'search': True})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/')

    return render (request, 'product/product-list.html', {'search': True, 'message': messages})

def subscription(request):
    if request.method=='POST':
        subscribe = request.POST.get('subs')
        Subscription.objects.get_or_create(email=subscribe)
    return HttpResponseRedirect('/')


class ContactView(TemplateView):
    template_name = 'product/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['about'] = AboutITeam.objects.last()
