# store/urls.py
from django.urls import path
from . import views
from store.views import like_toggle

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:cat_id>/', views.category_products, name='category_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.all_products, name='all_products'),
    path('profile/', views.profile, name='profile'),
    path('location/', views.location, name='location'),
    path('likes/', views.likes_view, name='likes'),
    path('product/<int:pk>/like/', like_toggle, name='like_toggle'),
]