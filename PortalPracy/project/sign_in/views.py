from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def index(request):
    return render(request, 'sign_in/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('offerts:index')
    else:
        form = UserRegisterForm()
    return render(request, 'sign_in/register.html', {'form': form})
