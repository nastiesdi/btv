# Generated by Django 3.0.3 on 2020-04-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200410_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=150.0, max_digits=15),
        ),
    ]
