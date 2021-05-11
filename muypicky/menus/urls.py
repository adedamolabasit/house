from django.urls import path
from .views import (
   
    
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView,
    
    
)
app_name='menus'

urlpatterns = [
    path('create/',ItemCreateView.as_view(),name='create'),  
    path('',ItemListView.as_view(),name='list'), 
    path('<int:pk>/',ItemDetailView.as_view(),name='details'),   
    path('<int:pk>/edit/',ItemUpdateView.as_view(),name='update-view'),   



]
