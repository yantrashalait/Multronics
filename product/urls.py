from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('notifications/<int:pk>/', views.view_notifications, name='notification'),
    path('wishlists/<int:pk>/', views.view_wishlist, name='wishlist'),
    path('cart/<int:pk>/', views.view_cart, name='cart'),
    path('product/list/', views.ProductList.as_view(), name='product_list'),
    path('product/add/', views.ProductAdd.as_view(), name='product_add'),

    # for notifications
    path('notification/view/<int:pk>/', views.see_notification, name='see_notification'),
]