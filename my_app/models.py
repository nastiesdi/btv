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
    idd=models.IntegerField()
    name = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    image = models.ImageField(blank=True, upload_to='e')
    description = models.CharField(max_length=20000)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=150.00)

    def __str__(self):
        return '{} {}'.format(self.name, self.model)

    def load_tv(self, file):
        with open(file, 'r') as infile:
            reader = csv.DictReader(infile, delimiter=',')
            for line in reader:
                self.objects.create(name=line['name'], model=line['model'], url=line['url'],
                                    description=line['description'])
