
from django.shortcuts import render
import json

from .models import Search, Products

from django.views import generic



BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
'https://images.craigslist.org/00F0F_8FJ6PlvN7vX_300x300.jpg'
'https://images.craiglist.org/00F0F_77EyfQN0DiD_300x300.jpg'
PRODUCT_DICT = {'tv': 'Электроника / ТВ и Аксессуары / Телевизоры',
                'washer': 'Для дома / Бытовая техника / Стиральные машины',
                'stove': 'Для кухни / Встраиваемая техника / Варочные панели',
                'hods': 'Для кухни / Встраиваемая техника / Вытяжки',
                'microwaves': 'Для кухни / Мелкая бытовая техника / Микроволновые печи',
                'dishwashers': 'Для кухни / Крупная бытовая техника / Посудомоечные машины',
                'refrigerators': 'Для кухни / Крупная бытовая техника / Холодильники',
                'ovens': 'Для кухни / Встраиваемая техника / Духовые шкафы',
                'freezer': 'Для кухни / Крупная бытовая техника / Морозильники',
                'tabletops': 'Для кухни / Крупная бытовая техника / Настольные плиты',
                'coffeemakers':'Для кухни / Мелкая бытовая техника / Кофеварки и кофемашины'}


class ProductListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 18


class SearchListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        q = self.request.GET.get('search')
        q = q.replace(" ", "+")
        context['search'] = q
        context['link'] = f'?search={q}&page='
        return context

    def get_queryset(self):
        search = self.request.GET.get('search').rstrip().lstrip()
        for each in range(-1, -100, -1):
            search =search[:each]
            new_search = search.lower().title()
            object_list = Products.objects.filter(name__icontains=search) | Products.objects.filter(model__icontains=search) | Products.objects.filter(name__icontains=new_search) | Products.objects.filter(model__icontains=new_search)
            if object_list:
                return object_list


class CatalogListView(generic.ListView):
    model = Products
    template_name = 'my_app/product-list.html'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['link'] = '?page='
        return context

    def get_queryset(self):
        object_list = Products.objects.filter(category__icontains=PRODUCT_DICT.get(self.kwargs['product']))
        return object_list


def home(request):
    return render(request, 'my_app/main.html')


def catalog(request):
    return render(request, 'my_app/catalog.html')


def product(request, productid):
    all_tv = Products.objects.all()
    product = None
    for each in all_tv:
        if each.id == int(productid):
            product = each
            break
    stuff_for_frontend = {'product': product}
    return render(request, 'my_app/product.html', stuff_for_frontend)


def contacts(request):
    return render(request, 'my_app/сontacts.html')


def payment(request):
    return render(request, 'my_app/payment.html')


def new_search(request):
    with open(r'E:\untitled\db.json', 'r') as infile:
        reader = json.loads(infile.read())
        for line in reader:
            try:
                line.get('Сервисные центры')
            except:
                servise_centre = None
            else:
                servise_centre = line.get('Категория')
            Products.objects.create(category=line['Категория'],
                                    name=line['Товар'],
                                    model=line['Бренд'],
                                    article=line['Артикул'],
                                    url=line['Изображения'],
                                    anotation=line['Аннотация'],
                                    description=line['Описание'],
                                    price=line['[n]Цена'],
                                    title_page=line['Заголовок страницы'],
                                    key_word=line['Ключевые слова'],
                                    page_description=line['Описание страницы'],
                                    importer=line['Импортер'],
                                    servise_centre=servise_centre,
                                    garancy=line['Гарантия мес'],
                                    img_id=line['img_id'])
    # Products.objects.all().delete()
    return render(request, 'base.html')
