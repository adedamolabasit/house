# Generated by Django 2.2 on 2020-05-07 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='conents',
            new_name='contents',
        ),
    ]