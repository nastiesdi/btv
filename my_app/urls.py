from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('catalog/<str:product>/', views.product, name='payment')
]