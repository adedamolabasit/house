from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import get_user_model,authenticate,login
from django.http import Http404
from pro.models import RestaurantLocation
from menus.models import Item 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,View
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
User=get_user_model()

class ProfileFollow(LoginRequiredMixin,View):
    def post(self,request,*args,**kwargs):
        User=self.request.user.username
        # print(request.data)
        print(request.POST)
        print(User)
        return redirect(f'profile/{User}')
    
        
class ProfileDetailView(LoginRequiredMixin,DetailView):
        template_name='profiles/user.html'
        def get_object(self):
            username=self.kwargs.get('profiles')
            if username is None:
                raise Http404
            queryset=get_object_or_404(User,username__iexact=username,is_active=True)
            return queryset
        def get_context_data(self,*args,**kwargs):
            context=super(ProfileDetailView,self).get_context_data(*args,**kwargs)
            user=context['user']
            query=self.request.GET.get('q')
            items_exists=Item.objects.filter(user=user).exists()
            qs = RestaurantLocation.objects.filter(owner=user).search(query)   
            if items_exists and qs.exists():
                context['locations']=qs
            return context    
def login_view(request):
    next=request.GET.get('next')
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(email=email,password=password)
        login(request,user)
        if next:
            return redirect('login')
        return redirect('/')
    context={'form':form}
    template_name='profiles/login.html'
    return render(request,template_name,context)

    


