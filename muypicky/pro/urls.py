from django.urls import path
from pro import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .views import (
   
    RestaurantListView,
    RestaurantDetailListView,
    RestaurantcreateView,
    RestaurantUpdateView,
    RestaurantCatListView,   
)



urlpatterns = [
    path('',TemplateView.as_view(template_name='pro/home.html'),name='homeview'),
    path('contact',TemplateView.as_view(template_name='pro/contact.html'),name='contactview'),
    path('about',TemplateView.as_view(template_name='pro/about.html'),name='aboutview'),
    path('restaurant/<str:slug>/',RestaurantCatListView.as_view(),name='restaurantcat'),
    path('restaurant/<slug:slug>',RestaurantDetailListView.as_view() ,name='details'),
    path('restaurant',RestaurantListView.as_view(),name='restaurant-list'),
    path('restaurant-upload',RestaurantcreateView.as_view(),name='create'),   
    path('restaurant/<slug:slug>/edit/',RestaurantUpdateView.as_view(),name='edit'),   
    path('login/',LoginView.as_view(),name='login'),   
]
