from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.conf import settings
from django.db.models import Q

from django.shortcuts import reverse
class RestaurantLocationQuerySet(models.QuerySet):
    def search(self,query):
        if query:
            query=query.strip()
            return self.filter(
            Q(name__icontains=query)|
            Q(location__icontains=query)|
            Q(location__iexact=query)|
            Q(category__icontains=query)|
            Q(item__name__icontains=query)|
            Q(item__contents__icontains=query)|
            Q(item__excludes__icontains=query)
                ).distinct()
        return self

class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model,using=self._db)
    def search(self,query):
        return self.get_queryset().search(query)




User=settings.AUTH_USER_MODEL
# Create your models here.
class RestaurantLocation(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=False)
    location= models.CharField(max_length=100,null=True ,blank=True)
    category=models.CharField(max_length=200,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True)

    objects=RestaurantLocationQuerySet.as_manager()
    class Meta:
        ordering=['-updated','-timestamp']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('details',kwargs={'slug':self.slug})
    
    @property
    def title(self):
        return f'{self.name}-{self.owner}-{self.pk}'
def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    # print('saving...')
    # print(instance.timestamp)
    instance.category=instance.category.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug=unique_slug_generator(instance)
#         instance.save

pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)
# post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)

