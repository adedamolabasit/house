from django import forms
from .models import *
from dam.models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=[
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public',
        ]


    def __init__(self,user=None,*args,**kwargs):
        super(ItemForm,self).__init__(*args,**kwargs)
        self.fields['restaurant'].queryset=RestaurantLocation.objects.all().filter(owner=user)
        return super(ItemForm,self).__init__(*args,**kwargs)