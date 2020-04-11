import requests
from django.shortcuts import render
from requests.compat import quote_plus
from .models import Search, Products
from bs4 import BeautifulSoup
# from . import models
import csv

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
'https://images.craigslist.org/00F0F_8FJ6PlvN7vX_300x300.jpg'
'https://images.craiglist.org/00F0F_77EyfQN0DiD_300x300.jpg'


#
# def home(request):
#     return render(request, 'base.html')

def home(request):
    all_tv = Products.objects.all()
    print(all_tv)
    final_postings = []
    for each in all_tv:
        print(each.id)
        final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.image])
    stuff_for_frontend = {
        'search': 'ddddd',
        'summary': final_postings, }
    return render(request, 'my_app/catalog.html', stuff_for_frontend)

def catalog(request):
    all_tv = Products.objects.all()
    final_postings = []
    for each in all_tv:
        final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.image])
    stuff_for_frontend = {
        'search': 'ddddd',
        'summary': final_postings, }
    return render(request, 'my_app/catalog.html', stuff_for_frontend)

def product(request, product):
    # request.GET.get()
    product_dict = {'tv': 'телевизор', 'washer': 'стиральная машина', 'stove':'варочная панель', 'hods': 'вытяжка', 'microwaves': 'микроволновая печь', 'dishwashers': 'посудомоечная машина', 'refrigerators':'холодильник', 'ovens': 'духовой шкаф'}
    all_tv = Products.objects.all()
    final_postings = []
    print(product_dict[product])
    for each in all_tv:
        if each.name.lower().lstrip().rstrip() == product_dict[product]:
            final_postings.append([f'{each.idd}.jpg', each.name, each.model, each.image])
    stuff_for_frontend = {
        'search': 'ddddd',
        'summary': final_postings, }
    return render(request, 'my_app/catalog.html', stuff_for_frontend)


def contacts(request):
    return render(request, 'my_app/сontacts.html')

def payment(request):
    return render(request, 'my_app/payment.html')


def new_search(request):
    with open('E:\parser\\test.csv', 'r') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        for line in reader:
            Products.objects.create(idd=line['id'], name=line['name'].lower().lstrip().rstrip(), model=line['model'], url=line['url'],
                                    description=line['description'])
    # Products.objects.all().delete()
    return render(request, 'base.html')
