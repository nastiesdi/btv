# Generated by Django 3.0.3 on 2020-05-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_products_img_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='anotation',
            field=models.TextField(default=None, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(default=None, max_length=20000, null=True),
        ),
    ]