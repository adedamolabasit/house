# Generated by Django 3.2 on 2021-05-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0002_auto_20210503_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
