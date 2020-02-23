import requests
from django.shortcuts import render
from requests.compat import quote_plus
from .models import Search
from bs4 import BeautifulSoup
from . import models
# Create your views here.

BASE_CRAIGSLIST_URL='https://www.21vek.by/refrigerators/'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL+(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('div',{'id': 'j-search_result'})
    print(post_titles)
    stuff_for_frontend  = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)