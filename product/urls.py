from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),

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

    # crud for products
    path('product/list/', views.ProductList.as_view(), name='product-list'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),

    # crud for banner images
    path('banner/list/', views.BannerList.as_view(), name='banner-list'),
    path('banner/create/', views.BannerCreate.as_view(), name='banner-create'),
    path('banner/<int:pk>/delete/', views.BannerDelete.as_view(), name='banner-delete'),
    path('banner/<int:pk>/update/', views.BannerUpdate.as_view(), name='banner-update'),

    # view all notifications of user
    path('notifications/<int:pk>/', views.NotificationListView.as_view(), name='notification'),
    # view all waitlists of user
    path('waitlist/<int:pk>/', views.WaitListView.as_view(), name='waitlist'),
    # view all cart of user
    path('cart/<int:pk>/', views.CartListView.as_view(), name='cart'),
    # view all favourites of user
    path('favourite/<int:pk>/', views.FavouriteListView.as_view(), name='favourite'),

    # mark a notification as seen
    path('notification/view/<int:pk>/', views.see_notification, name='see-notification'),

    # add to favourite
    path('favourite/add/', views.add_to_favourite, name='add_favourite'),
]
