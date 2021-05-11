from django import forms 
from django.contrib.auth import get_user_model,authenticate

# from django.conf.auth import get_user_model,authenticate



class UserLoginForm(forms.Form):
    # username=forms.CharField(max_length=50)
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')

        if email and password:
            user=authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('wrong password')
            if not user.is_active:
                raise forms.ValidationError('this user is no more active')
        return super(UserLoginForm,self).clean(*args,**kwargs)