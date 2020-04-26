# import requests
from django.shortcuts import render
# from requests.compat import quote_plus
from .models import Search, Products
# from bs4 import BeautifulSoup
from . import models
import csv

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
'https://images.craigslist.org/00F0F_8FJ6PlvN7vX_300x300.jpg'
'https://images.craiglist.org/00F0F_77EyfQN0DiD_300x300.jpg'
PRODUCT_DICT = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove': 'варочная панель', 'hods': 'вытяжка',
                'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина',
                'refrigerators': 'холодильник', 'ovens': 'духовой шкаф'}


def home(request):
    all_tv = Products.objects.all()
    final_postings = []
    for each in all_tv:
        final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.image])
    stuff_for_frontend = {
        'summary': final_postings}
    return render(request, 'my_app/main.html')


def catalog(request):
    product_dict = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove': 'варочная панель', 'hods': 'вытяжка',
                    'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина',
                    'refrigerators': 'холодильник', 'ovens': 'духовой шкаф'}
    final_postings = []
    all_tv = Products.objects.all()
    for each in product_dict.values():
        for product in all_tv:
            if product.name.lower().lstrip().rstrip() == each:
                final_postings.append([f'{product.idd}.jpg', product.name, product.model, product.description, product.price])
                break
    stuff_for_frontend = {'summary': final_postings}
    return render(request, 'my_app/catalog.html', stuff_for_frontend )


def product(request, productid):
    all_tv = Products.objects.all()
    product=None
    for each in all_tv:
        if each.idd == int(productid):
            product = {'img': f'{each.idd}.jpg', 'name': each.name, 'model': each.model, 'description': each.description, 'price': each.price, 'idd': each.idd}
            break
    stuff_for_frontend = {'product': product}
    print(stuff_for_frontend)
    return render(request, 'my_app/product.html', stuff_for_frontend)


def list_product(request, product):
    product_dict = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove':'варочная панель', 'hods': 'вытяжка', 'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина', 'refrigerators':'холодильник', 'ovens': 'духовой шкаф'}
    all_tv = Products.objects.all()
    final_postings = []
    for each in all_tv:
        if each.name.lower().lstrip().rstrip() == product_dict[product]:
            final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.description, each.price, each.idd])
    stuff_for_frontend = {
        'summary': final_postings}
    return render(request, 'my_app/catalog.html', stuff_for_frontend)


def list_product_from_main(request):
    all_tv = Products.objects.all()
    return render(request, 'my_app/catalog.html', stuff_for_frontend)


def contacts(request):
    return render(request, 'my_app/сontacts.html')


def payment(request):
    return render(request, 'my_app/payment.html')


def search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    final_postings = []
    all_tv = Products.objects.all()
    for each in all_tv:
        if search.lower().lstrip().rstrip() in each.name.lower().lstrip().rstrip() or search.lower().lstrip().rstrip() in each.model.lower().lstrip().rstrip():
            final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.description, each.price])
    stuff_for_frontend = {
        'search': '',
        'summary': final_postings, }
    return render(request, 'my_app/catalog.html', stuff_for_frontend)


def new_search(request):
    # with open('E:\parser\\test.csv', 'r') as infile:
    #     reader = csv.DictReader(infile, delimiter=',')
    #     for line in reader:
    #         Products.objects.create(idd=line['id'], name=line['name'].lower().lstrip().rstrip(), model=line['model'], url=line['url'],
    #                                 description=line['description'])
    # Products.objects.all().delete()
    return render(request, 'base.html')


