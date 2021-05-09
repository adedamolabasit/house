from django.urls import path 
from .views import (
    RestaurantListView,
    ContactView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView,
    # restaurant_createview
    )

app_name='dam'


urlpatterns=[
    path('',RestaurantListView.as_view(),name='home'),
    path('restaurant/a/<slug:slug>',RestaurantListView.as_view(),name='restaurant_list' ),
    path('<slug:slug>',RestaurantDetailView.as_view(),name='restaurant_detail' ),
    path('<slug:slug>/update',RestaurantUpdateView.as_view(),name='update' ),
    path('contact/',ContactView.as_view(),name='contact'),
    path('restaurant/create/',RestaurantCreateView.as_view(),name='contact'),

]