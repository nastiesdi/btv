from django.urls import path
from django.urls import re_path
from django.conf.urls import url
from django.conf.urls import handler400, handler500
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'product/(?P<productid>\d+)/', views.product, name='product'),
    path('wrong_field', views.home, name='home'),
    path('main', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    re_path(r'^contacts', views.contacts, name='contacts'),
    path('payment', views.payment, name='payment'),
    path('catalog/<str:product>/', views.CatalogListView.as_view(), name='payment'),
    url(r'catalog$', views.catalog, name='catalog'),
    path('search', views.SearchListView.as_view(), name='search'),

]