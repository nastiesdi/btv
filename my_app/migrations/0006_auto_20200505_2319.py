# Generated by Django 3.0.3 on 2020-05-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_auto_20200505_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='idd',
            field=models.IntegerField(default=None),
        ),
    ]