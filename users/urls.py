from django.urls import path, re_path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/create/', views.profile_create, name='profile-create'),
    path('profile/update/<int:pk>/', views.profie_update, name='profile-update'),
]