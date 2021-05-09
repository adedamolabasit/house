from django.conf import settings 
from django.db import models
from django.db.models.signals import pre_save, post_save 
from .utils import unique_slug_generator
from django.urls import reverse

User=settings.AUTH_USER_MODEL
# Create your models here.
class RestaurantLocation(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    location =models.CharField(max_length=120,null=True,blank=True)
    category=models.CharField(max_length=120,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='restaurant_logo')
    slug=models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('dam:restaurant_detail',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('dam:update',kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name        
def pre_save_reciever(sender,instance,*args,**kwargs):

    print('saving..')
    print('instance.timestamp')
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

def post_save_reciever(sender,instance,created,*args,**kwargs):
    print('saved')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

pre_save.connect(pre_save_reciever,sender=RestaurantLocation)
post_save.connect(post_save_reciever,sender=RestaurantLocation)