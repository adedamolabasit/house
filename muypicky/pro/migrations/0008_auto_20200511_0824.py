# Generated by Django 2.2 on 2020-05-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0007_auto_20200507_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]