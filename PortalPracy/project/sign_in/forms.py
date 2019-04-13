from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False) #default: required=True

    class Meta:
        model = User # model that is going to be affected when form.save() is done
        fields = ['username', 'email', 'password1', 'password2'] # fields that we want in the form and in that order
