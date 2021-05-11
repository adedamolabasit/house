from django import forms
from .models import RestaurantLocation
from .validators import validate_email,validate_category


class RestaurantCreateForm(forms.ModelForm):
    name=forms.CharField(required=True)
    email=forms.EmailField(validators=[validate_email])
    category=forms.CharField(required=False,validators=[validate_category])
    class Meta:
        model=RestaurantLocation
        fields=[
            'name',
            'location',
            'category',
        ]
    def clean_category(self):
        name=self.cleaned_data.get('name')
        owner=self.cleaned_data.get('owner')
        owner_object=RestaurantLocation.objects.all().filter(owner=owner)
        qs=RestaurantLocation.objects.filter(name=name)

        if qs.exists():
            raise forms.ValidationError(f'{name} has been created by you')
        return name

    # def clean_name(self,user=None):
    #     name=self.cleaned_data.get('name')
    #     qs=RestaurantLocation.objects.filter(name=name,owner=user)
    #     if qs.exists:
    #         raise forms.ValidationError(f'{name}:The restaurant name has been created')


    #     # def __init__(self,user=None,*args,**kwargs):
    #     # print(user)
    #     # super(ItemForm,self).__init__(*args,**kwargs)
    #     # self.fields['restaurant'].queryset=RestaurantLocation.objects.filter(owner=user)
  