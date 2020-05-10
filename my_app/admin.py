from django.contrib import admin
from .models import Search, Products
# Register your models here.
admin.site.register(Search)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'model', 'price']
    # list_display = [field.name for field in Products._meta.fields]
    # exclude = ['url'] # при переходе на товар в админке исключает отображение этого поля
    fields = ['idd', 'category', 'name', 'model', 'price'] #при переходе на товар в админке отображается только это поле
    list_filter = ['category']
    search_fields = ['model', 'description', 'name']
    class Meta:
        model = Products


admin.site.register(Products, ProductAdmin)
