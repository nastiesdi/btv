from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('wrong_field', views.home, name='home'),
    path('main', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('catalog/<str:product>/', views.list_product, name='payment'),
    path('search', views.search, name='search'),
    path('catalog', views.catalog, name='catalog'),
]