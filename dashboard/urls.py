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
    re_path(r'^add/specform-(?P<id>\d+)-title/$', views.newSpecificationTitle, name="title"),
    path('add/title/', views.newSpecificationTitle, name="title"),
    re_path(r'^add/specform-(?P<id>\d+)-content/$', views.newSpecificationContent, name="title"),
    path('add/content/', views.newSpecificationContent, name="content"),


    # crud for brands
    path('add/brand/', views.newBrand, name="brand"),
    path('brand/list/', views.BrandList.as_view(), name='brand-list'),
    path('brand/create/', views.BrandCreate.as_view(), name='brand-create'),
    path('brand/<int:pk>/delete/', views.BrandDelete.as_view(), name='brand-delete'),
    path('brand/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand-update'),

    # crud for banner images
    path('banner/list/', views.BannerList.as_view(), name='banner-list'),
    path('banner/create/', views.BannerCreate.as_view(), name='banner-create'),
    path('banner/<int:pk>/delete/', views.BannerDelete.as_view(), name='banner-delete'),
    path('banner/<int:pk>/update/', views.BannerUpdate.as_view(), name='banner-update'),

    path('product/list/', views.ProductList.as_view(), name="product-list"),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),

    path('specification/list', views.SpecificationList.as_view(), name='specification-list'),
    path('specification/add', views.SpecificationCreate.as_view(), name='specification-create'),
    path('specification/<int:pk>/update', views.SpecificationUpdate.as_view(), name="specification-update"),
    path('specification/<int:pk>/delete', views.SpecificationDelete.as_view(), name="specification-delete"),

    path('specification/<int:pk>/content/list', views.SpecificationContentList.as_view(), name="specification-content-list"),
    path('specification/<int:spec_id>/content/<int:pk>/delete', views.SpecificationContentDelete.as_view(), name="specification-content-delete"),

    path('about/create/', views.AboutCreate.as_view(), name='about-create'),
    path('about/<int:pk>/update/', views.AboutUpdate.as_view(), name='about-update'),

    path('product/<int:pk>/image/list/', views.ProductImageList.as_view(), name="product-images-list"),
    path('product/<int:product_id>/image/<int:pk>/delete/', views.ProductImageDelete.as_view(), name="product-image-delete"),
    path('product/<int:pk>/specification/list/', views.ProductSpecificationList.as_view(), name="product-specification-list"),
    path('product/<int:product_id>/specification/<int:pk>/delete/', views.ProductSpecificationDelete.as_view(), name="product-specification-delete"),
    # path('product/<int:product_id>/specification/<int:pk>/edit', views.ProductSpecificationEdit.as_view(), name="product-specification-edit"),

]
