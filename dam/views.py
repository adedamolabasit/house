from django.db.models import Q
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.views import View
from .models import RestaurantLocation
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .forms import RestaurantLocationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RestaurantListView(LoginRequiredMixin,ListView):
    template_name='dam/restaurantlocation_list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.all().filter(owner=self.request.user)
   
class RestaurantDetailView(DetailView):
    queryset=RestaurantLocation.objects.all()

class ContactView(TemplateView):
    template_name='dam/contact.html'  


def restaurant_createview(request):
    form=RestaurantLocationCreateForm(request.POST or None or  request.FILES)
    if form.is_valid():
        form.save()
        HttpResponseRedirect('/')
    context={'form':form}
    template_name='dam/form.html'
    return render(request,template_name,context)
    
class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class=RestaurantLocationCreateForm
    template_name='dam/form.html'
    success_url='/'
    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.owner=self.request.user
        return super(RestaurantCreateView,self).form_valid(form)
class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class=RestaurantLocationCreateForm
    template_name='dam/form_update.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context=super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
        context['update']:'update your restaurant location'   
        return context 
   

 
