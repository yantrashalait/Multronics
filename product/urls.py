from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),

    # crud for products
    path('product/list/', views.ProductList.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product/list/brand/<int:pk>/', views.brand_list, name='product-brand-list'),
    path('product/list/type/<int:pk>/', views.type_list, name='product-type-list'),
    path('product/list/super-deals/', views.super_deals_list, name='product-super-deals-list'),
    path('product/list/offer/', views.offer_list, name='product-offer-list'),
    path('product/list/most-viewed/', views.most_viewed_list, name='product-most-viewed-list'),
    path('search/', views.search_product, name='search-product'),

    # view all notifications of user
    path('notifications/<int:pk>/', views.NotificationListView.as_view(), name='notification'),
    # view all waitlists of user
    path('waitlist/<int:pk>/', views.WaitListView.as_view(), name='waitlist'),

    # view all cart of user
    path('cart/<int:pk>/', views.CartListView.as_view(), name='cart-list'),
    path('cart/add/', views.AddCart.as_view(), name='add-cart'),
    
    # view all favourites of user
    path('favourite/<int:pk>/', views.FavouriteListView.as_view(), name='favourite'),

    # mark a notification as seen
    path('notification/view/<int:pk>/', views.see_notification, name='see-notification'),

    # add to favourite
    path('favourite/add/', views.add_to_favourite, name='add_favourite'),

    #subscription
    path('subscription/', views.subscription, name='subscribe')
]
