from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    # crud for categories
    path('category/list/', views.CategoryList.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),

    # crud for brands
    path('brand/list/', views.BrandList.as_view(), name='brand-list'),
    path('brand/create/', views.BrandCreate.as_view(), name='brand-create'),
    path('brand/<int:pk>/delete/', views.BrandDelete.as_view(), name='brand-delete'),
    path('brand/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand-update'),

    # crud for types
    path('type/list/', views.TypeList.as_view(), name='type-list'),
    path('type/create/', views.TypeCreate.as_view(), name='type-create'),
    path('type/<int:pk>/delete/', views.TypeDelete.as_view(), name='type-delete'),
    path('type/<int:pk>/update/', views.TypeUpdate.as_view(), name='type-update'),

    # crud for banner images
    path('banner/list/', views.BannerList.as_view(), name='banner-list'),
    path('banner/create/', views.BannerCreate.as_view(), name='banner-create'),
    path('banner/<int:pk>/delete/', views.BannerDelete.as_view(), name='banner-delete'),
    path('banner/<int:pk>/update/', views.BannerUpdate.as_view(), name='banner-update'),

    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),

    
]