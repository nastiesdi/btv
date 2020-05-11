from django.db import models
import os
import csv


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'


class Products(models.Model):
    idd = models.IntegerField(default=None, null=True)
    category = models.CharField(max_length=500, default=None, null=True)
    name = models.CharField(max_length=500, null=True)
    model = models.CharField(max_length=500, null=True)
    article = models.CharField(max_length=500, default=None, null=True)
    url = models.CharField(max_length=500, null=True)
    image = models.ImageField(blank=True, upload_to='e', null=True)
    anotation = models.TextField(max_length=5000, default=None, null=True)
    description = models.TextField(max_length=20000, default=None, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=None, null=True)
    title_page = models.CharField(max_length=500, default=None, null=True)
    key_word = models.CharField(max_length=500, default=None, null=True)
    page_description = models.CharField(max_length=500, default=None, null=True)
    importer = models.CharField(max_length=500, default=None, null=True)
    servise_centre = models.CharField(max_length=500, default=None, null=True)
    make = models.CharField(max_length=500, default=None, null=True)
    garancy = models.CharField(max_length=10, default=None, null=True)
    img_id = models.IntegerField(null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.model)

    def load_tv(self, file):
        with open(file, 'r') as infile:
            reader = csv.DictReader(infile, delimiter=',')
            for line in reader:
                try:
                    line.get('Сервисные центры')
                except:
                    servise_centre = None
                else:
                    servise_centre = line.get('Категория')
                self.objects.create(category=line['Категория'],
                                    name=line['Товар'],
                                    model=line['Бренд'],
                                    article=line['Артикул'],
                                    url=line['Изображения'],
                                    anotation=line['Аннотация'],
                                    description=line['Описание'],
                                    price=line['Цена'],
                                    title_page=line['Заголовок страницы'],
                                    key_word=line['Ключевые слова'],
                                    page_description=line['Описание страницы'],
                                    importer=line['Импортер'],
                                    servise_centre=servise_centre,
                                    garancy=line['Гарантия мес'],
                                    img_id=line['img_id'])
