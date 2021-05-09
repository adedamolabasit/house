from django import forms 
from .models import RestaurantLocation


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model =RestaurantLocation 
        fields=[
            'name',
            'location',
            'category',
            'image',
        ]

    def clean_location(self):
        location=self.cleaned_data.get('location')
        if location == 'online':
            raise forms.ValidationError('Sorry we do not recommend {ONLINE RESTAURANT} ')
        return location 