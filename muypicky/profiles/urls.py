from django.urls import path
from .views import ProfileDetailView,login_view,ProfileFollow
app_name='profiles'
urlpatterns = [
    path('profile/<slug:profiles>',ProfileDetailView.as_view(),name='profile'),
    path('login/now',login_view,name='login'),
    path('profile-follow',ProfileFollow.as_view(),name='follow'),
  
]