from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.db.models import Q
from .forms import RestaurantCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


from .models import RestaurantLocation

# Create your views here.
class RestaurantListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        queryset=RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset

class RestaurantCatListView(LoginRequiredMixin,ListView):
    queryset=RestaurantLocation.objects.all
    def get_queryset(self):
        slug=self.kwargs.get('slug')    
        if slug:
            queryset=RestaurantLocation.objects.filter(
                Q(owner=self.request.user,category__iexact=slug)|
                Q(owner=self.request.user,category__icontains=slug)
            )
        else:
            queryset=RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset   
class RestaurantDetailListView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        queryset=RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset
class RestaurantcreateView(LoginRequiredMixin,CreateView):
    form_class=RestaurantCreateForm
    template_name='pro/form.html'
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(RestaurantcreateView,self).form_valid(form)
    def get_context_data(self,*args,**kwargs):
        context=super(RestaurantcreateView,self).get_context_data(*args,**kwargs)
        context['text']='upload your fucking items'
        return context
    # def get_form_kwargs(self):
    #     kwargs=super(RestaurantcreateView,self).get_form_kwargs()
    #     kwargs['user']=self.request.owner
    #     # kwargs['instance']=Item.objects.filter(user=self.request.user).first()
    #     return kwargs

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class=RestaurantCreateForm
    template_name='pro/form.html'
    def get_context_data(self,*args,**kwargs):
        name=self.get_object().name
        created=self.get_object().timestamp

        context=super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
        context['text']=f'edit your restaurant list:{name} which was created on {created} '
        return context
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        form_valid=super(RestaurantUpdateView,self).form_valid(form)
        return form_valid
    def get_queryset(self):
        queryset=RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset

    
    
        



    

