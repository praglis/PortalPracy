from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def index(request):
    return render(request, 'sign_in/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratolations {username}! Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'sign_in/register.html', {'form': form})

@login_required # decorator - adds functionality to an existing function
def profile(request):
    return render(request, 'sign_in/profile.html')
