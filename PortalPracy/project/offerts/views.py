from django.shortcuts import render
from django.http import HttpResponse

from .models import JobOffert, Company, Localisation

def index(request):
    offert_list = JobOffert.objects.all()
    context = {'offert_list' : offert_list}
    
    return render(request, 'offerts/index.html', context)

def details(request, offert_id):
    try:
        offert = JobOffert.objects.get(pk=offert_id)
    except JobOffert.DoesNotExist:
        raise Http404("Offert does not exist")
    return render(request, 'offerts/details.html', {'offert' : offert})