from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),

    # crud for products
    path('product/list/', views.ProductList.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/list/category/<int:pk>', views.CategoryListView.as_view(), name='product-category-list'),
    path('product/list/brand/<int:pk>/', views.BrandListView.as_view(), name='product-brand-list'),
    path('product/list/super-deals/', views.SuperDealsListView.as_view(), name='product-super-deals-list'),
    path('product/list/offer/', views.OfferListView.as_view(), name='product-offer-list'),
    path('product/list/most-viewed/', views.MostViewedListView.as_view(), name='product-most-viewed-list'),
    path('search/', views.search_product, name='search-product'),    
    path('contact', views.ContactView.as_view(), name="contact"),

]
