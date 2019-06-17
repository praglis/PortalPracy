from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import template

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AccountTypeForm

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        acc_type_form = AccountTypeForm(request.POST)

        if user_form.is_valid() and acc_type_form.is_valid():
            new_user = user_form.save()
            acc_type_form.set_group(new_user)
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}! Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        acc_type_form = AccountTypeForm()

    context = {
        'user_form': user_form,
        'acc_type_form': acc_type_form
    }
    return render(request, 'sign_in/register.html', context)

@login_required # decorator - adds functionality to an existing function
def profile(request):
    if request.method == "POST": # when we possibly pass a new data
        u_form = UserUpdateForm(request.POST, instance=request.user) # request.POST to pass in data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # request.FILE additional file data - pictures

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'sign_in/profile.html', context)

def LogoutView(request):
    logout(request)
    messages.success(request, f'Succesfully logged out!')
    return redirect('home')
