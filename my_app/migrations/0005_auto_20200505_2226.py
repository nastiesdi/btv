# Generated by Django 3.0.3 on 2020-05-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20200502_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='anotation',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AddField(
            model_name='products',
            name='article',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='garancy',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='products',
            name='importer',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='key_word',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='make',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='page_description',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='servise_centre',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='products',
            name='title_page',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(default=None, max_length=20000),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=15),
        ),
    ]
