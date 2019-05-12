from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileCreationForm


def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #user_form.save()
            profile_form.instance = user_form.save().profile
            profile_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}! Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileCreationForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
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
