import requests
from django.shortcuts import render
from requests.compat import quote_plus
from .models import Search, Tv
from bs4 import BeautifulSoup
# from . import models
import csv

# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
'https://images.craigslist.org/00F0F_8FJ6PlvN7vX_300x300.jpg'
'https://images.craiglist.org/00F0F_77EyfQN0DiD_300x300.jpg'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    Search.objects.create(search=search)
    #     final_postings.append([post_title, post_url, post_price, post_image_url])
    # stuff_for_frontend = {
    #     'search': search,
    #     'summary': final_postings,
    # }
    # return render(request, 'my_app/new_search.html', stuff_for_frontend)


def new_search(request):
    with open('E:\parser\\test.csv', 'r') as infile:
        reader = csv.DictReader(infile, delimiter=',')
        for line in reader:
            Tv.objects.create(idd=line['id'], name=line['name'], model=line['model'], url=line['url'],
                                description=line['description'])
    # Tv.objects.all().delete()
    return render(request, 'base.html')
