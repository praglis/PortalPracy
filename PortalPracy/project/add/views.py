from django.shortcuts import render
from django.http import HttpResponse

def offert(request):
    return render(request, 'add/offert.html')

def form(request):
    return render(request, 'add/form.html')

def apply(request):
    return render(request, 'add/apply.html')
