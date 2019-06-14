from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']

class AccountTypeForm(forms.Form):
    user_groups = (
        ('candidates', 'candidate'),
        ('employers', 'employer'),
        )
    account_type = forms.ChoiceField(choices=user_groups)

    def set_group(self, new_user):
        new_user_group = self.cleaned_data.get('account_type')
        group = Group.objects.get(name=new_user_group)
        group.user_set.add(new_user)

class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(required=False)
    cv = forms.FileField(required=False)
    class Meta:
        model = Profile
        fields = ['phone', 'image', 'cv']
