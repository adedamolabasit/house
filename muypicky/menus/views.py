from django.shortcuts import render,get_object_or_404
from .models import Item
from .forms import ItemForm
from django.views.generic import CreateView,DetailView,UpdateView,ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ItemListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.all().filter(user=self.request.user)
class ItemCreateView(LoginRequiredMixin,CreateView):
    form_class=ItemForm
    template_name='menus/form.html'
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        return super(ItemCreateView,self).form_valid(form)
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        context=super(ItemCreateView,self).get_context_data(*args,**kwargs)
        context['title']='create item here'
        return context
    def get_form_kwargs(self):
        kwargs=super(ItemCreateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        # kwargs['instance']=Item.objects.filter(user=self.request.user).first()
        return kwargs

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    form_class=ItemForm
    template_name='menus/form.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context=super(ItemUpdateView,self).get_context_data(*args,**kwargs)
        context['title']='edit data here'
        return context

    def get_form_kwargs(self):
        kwargs=super(ItemUpdateView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        # kwargs['instance']=Item.objects.filter(user=self.request.user).first()
        return kwargs
