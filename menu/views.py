from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView

from .forms import *
from dam.models import *
from django.contrib.auth import get_user_model

User=get_user_model()
class ItemListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
class ItemDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
class ItemCreateView(LoginRequiredMixin,CreateView):
    form_class=ItemForm
    template_name='menu/forms.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def form_valid(self,form):
        instance=form.save(commit=False)
        return super(ItemCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs=super(ItemCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


    def get_context_data(self,*args,**kwargs):
        context=super(ItemCreateView,self).get_context_data(*args,**kwargs)
        context['update']='Add Menu items to your Restaurant'
        return context

 

        
class ItemUpdateView(UpdateView):
    form_class=ItemForm
    template_name='menu/update_form.html'
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ItemUpdateView,self).get_context_data(*args,**kwargs)
        context['update']:'Edit'
        return context 

class Profile(DetailView):
    template_name='menu/profile.html'

    def get_object(self):
        kwargs=self.kwargs.get('slug')
        return User.objects.filter(username__iexact=kwargs,is_active=True)

    def get_context_data(self,*args,**kwargs):
        context=super(Profile,self).get_context_data(*args,**kwargs)
        query=self.request.GET.get('q')      
        items_exists=Item.objects.filter(user=self.request.user).exists()
        qs=RestaurantLocation.objects.filter(owner=self.request.user)
        if query:
            qs=qs.filter(name__contains=query)
        if items_exists and qs.exists():
            context['locations']=qs
        return context
      