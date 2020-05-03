# import requests
from django.shortcuts import render
# from requests.compat import quote_plus
from .models import Search, Products
# from bs4 import BeautifulSoup
from . import models
import csv
from django.views import generic

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
'https://images.craigslist.org/00F0F_8FJ6PlvN7vX_300x300.jpg'
'https://images.craiglist.org/00F0F_77EyfQN0DiD_300x300.jpg'
PRODUCT_DICT = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove': 'варочная панель', 'hods': 'вытяжка',
                'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина',
                'refrigerators': 'холодильник', 'ovens': 'духовой шкаф'}


class ProductListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 15


class SearchListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 15


    def get_queryset(self):
        search = self.request.GET.get('search')
        object_list = Products.objects.filter(name__icontains=search) | Products.objects.filter(model__icontains=search)
        return object_list


class CatalogListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 15

    def get_queryset(self):
        product_dict = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove': 'варочная панель', 'hods': 'вытяжка',
                        'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина',
                        'refrigerators': 'холодильник', 'ovens': 'духовой шкаф'}
        object_list = Products.objects.filter(name__icontains=product_dict.get(self.kwargs['product']))
        return object_list


def home(request):
    return render(request, 'my_app/main.html')


def catalog(request):
    return render(request, 'my_app/catalog.html')


def product(request, productid):
    all_tv = Products.objects.all()
    product = None
    for each in all_tv:
        if each.idd == int(productid):
            product = {'img': f'{each.idd}.jpg', 'name': each.name, 'model': each.model,
                       'description': each.description.replace(';', ';</strong></br>').replace(':',':<strong>'), 'price': each.price, 'idd': each.idd}
            break
    stuff_for_frontend = {'product': product}
    print(stuff_for_frontend)
    return render(request, 'my_app/product.html', stuff_for_frontend)

def contacts(request):
    return render(request, 'my_app/сontacts.html')


def payment(request):
    return render(request, 'my_app/payment.html')




def new_search(request):
    # with open('E:\parser\\test.csv', 'r') as infile:
    #     reader = csv.DictReader(infile, delimiter=',')
    #     for line in reader:
    #         Products.objects.create(idd=line['id'], name=line['name'].lower().lstrip().rstrip(), model=line['model'], url=line['url'],
    #                                 description=line['description'])
    # Products.objects.all().delete()
    return render(request, 'base.html')
