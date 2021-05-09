from django.db import models
from django.conf import settings
from dam.models import RestaurantLocation
from django.urls import reverse

# Create your models here.
User=settings.AUTH_USER_MODEL
class Item(models.Model):
    # association
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(RestaurantLocation,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    contents=models.TextField(help_text='seperate each item by comma')
    excludes=models.TextField(blank=True,null=True,help_text='seperate each item by comma')
    public=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



    class Meta:
        ordering=['-updated','-timestamp']

    def get_contents(self):
        return self.contents.split(',')
    def get_excludes(self):
        return self.excludes.split(',')

    def get_absolute_url(self):
        return reverse('menu:detail',kwargs={'pk':self.pk})
    def get_update_url(self):
        return reverse('menu:update',kwargs={'pk':self.pk})
   