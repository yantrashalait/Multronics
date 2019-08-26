from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('notifications/<int:pk>/', views.view_notifications, name='notification'),
    path('wishlists/<int:pk>/', views.view_waitlist, name='wishlist'),
    path('cart/<int:pk>/', views.view_cart, name='cart'),
    path('favourite/<int:pk>/', views.view_favourite, name='favourite'),
    path('product/list/', views.ProductList.as_view(), name='product-list'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),

    # for notifications
    path('notification/view/<int:pk>/', views.see_notification, name='see-notification'),
    path('product/<int:pk>/update', views.ProductUpdate.as_view(), name='product-update'),
]
