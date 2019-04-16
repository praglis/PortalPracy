from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default: required=True

    class Meta:
        model = User # model that is going to be affected when form.save() is done
        fields = ['username', 'email', 'password1', 'password2'] # fields that we want in the form and in that order

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    cv = forms.FileField(required=False)
    class Meta:
        model = Profile
        fields = ['phone', 'image', 'cv']
