from django.urls import path

from .views import *
app_name='menu'


urlpatterns=[
    path('',ItemListView.as_view(),name='list'),
    path('<int:pk>/',ItemDetailView.as_view(),name='detail'),
    path('<slug:slug>/profile/',Profile.as_view(),name='profile'),
    path('create/',ItemCreateView.as_view(),name='create'),
    path('<int:pk>/update/',ItemUpdateView.as_view(),name='update'),

]
