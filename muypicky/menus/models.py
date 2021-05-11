from django.db import models
from django.conf import settings
from pro.models import RestaurantLocation
from django.shortcuts import reverse


# Create your models here.
User=settings.AUTH_USER_MODEL

class Item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(RestaurantLocation,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    contents=models.TextField(help_text='seperate each item by comma')
    excludes=models.TextField(blank=True,null=True,help_text='seperate each items by comma')
    public=models.BooleanField(default=True)
    timestamp    =models.DateTimeField(auto_now_add=True)
    updated      =models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-updated','-timestamp']
    def get_contents(self):
        return self.contents.split(",")
    def get_excludes(self):
        return self.excludes.split(",")
    def get_absolute_url(self):
        return reverse('menus:details',kwargs={'pk':self.pk})
   

    def __str__(self):
        return self.name