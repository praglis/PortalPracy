from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'add/index.html')

def apply(request):
    return render(request, 'add/apply.html')
