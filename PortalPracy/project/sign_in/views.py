from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'sign_in/index.html')

def signup(request):
    form = UserCreationForm()
    return render(request, 'sign_in/signup.html', {'form': form})
