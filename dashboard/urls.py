from django.urls import path, re_path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    # crud for categories
    path('category/list/', views.CategoryList.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    re_path(r'^add/specform-(?P<id>[0-9])-title/$', views.newSpecificationTitle, name="title"),
    path('add/title/', views.newSpecificationTitle, name="title"),
    re_path(r'^add/specform-(?P<id>[0-9])-content/$', views.newSpecificationContent, name="title"),
    path('add/content/', views.newSpecificationContent, name="content"),


    # crud for brands
    path('add/brand/', views.newBrand, name="brand"),
    path('brand/list/', views.BrandList.as_view(), name='brand-list'),
    path('brand/create/', views.BrandCreate.as_view(), name='brand-create'),
    path('brand/<int:pk>/delete/', views.BrandDelete.as_view(), name='brand-delete'),
    path('brand/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand-update'),

    # crud for types
    path('add/product_type/', views.newType, name="type"),
    path('type/list/', views.TypeList.as_view(), name='type-list'),
    path('type/create/', views.TypeCreate.as_view(), name='type-create'),
    path('type/<int:pk>/delete/', views.TypeDelete.as_view(), name='type-delete'),
    path('type/<int:pk>/update/', views.TypeUpdate.as_view(), name='type-update'),

    # crud for banner images
    path('banner/list/', views.BannerList.as_view(), name='banner-list'),
    path('banner/create/', views.BannerCreate.as_view(), name='banner-create'),
    path('banner/<int:pk>/delete/', views.BannerDelete.as_view(), name='banner-delete'),
    path('banner/<int:pk>/update/', views.BannerUpdate.as_view(), name='banner-update'),

    path('product/list/', views.ProductList.as_view(), name="product-list"),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),

    path('superimage/list/', views.SuperImageList.as_view(), name='superimage-list'),
    path('superimage/create/', views.SuperImageAdd.as_view(), name='superimage-create'),
    path('superimage/<int:pk>/update/', views.SuperImageUpdate.as_view(), name='superimage-update'),
    path('superimage/<int:pk>/delete/', views.SuperImageDelete.as_view(), name='superimage-delete'),

    path('offerimage/list/', views.OfferImageList.as_view(), name='offerimage-list'),
    path('offerimage/create/', views.OfferImageAdd.as_view(), name='offerimage-create'),
    path('offerimage/<int:pk>/update/', views.OfferImageUpdate.as_view(), name='offerimage-update'),
    path('offerimage/<int:pk>/delete/', views.OfferImageDelete.as_view(), name='offerimage-delete'),

    path('favourite/list/', views.FavouriteView.as_view(), name='favourite-list'),
    path('waitlist/list/', views.WaitListView.as_view(), name='wait-list'),
    path('bargain/list/', views.BargainView.as_view(), name='bargain-list'),

    path('order/list/', views.OrderList.as_view(), name='order-list'),
    path('order/detail/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('request/list/', views.RequestView.as_view(), name='request-list'),

    path('specification/list', views.SpecificationList.as_view(), name='specification-list'),
    path('specification/add', views.SpecificationCreate.as_view(), name='specification-create'),
    path('specification/<int:pk>/update', views.SpecificationUpdate.as_view(), name="specification-update"),
    
    path('about/list/', views.AboutList.as_view(), name='about-list'),
    path('about/create/', views.AboutCreate.as_view(), name='about-create'),
    path('about/<int:pk>/delete/', views.AboutDelete.as_view(), name='about-delete'),
    path('about/<int:pk>/update/', views.AboutUpdate.as_view(), name='about-update'),
]