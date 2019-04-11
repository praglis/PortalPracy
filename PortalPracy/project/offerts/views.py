from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Offert, Company, Agency

def index(request):
    offert_list = Offert.objects.all()
    context = {'offert_list' : offert_list}

    return render(request, 'offerts/index.html', context)

def details(request, offert_id):
    offert = get_object_or_404(Offert, pk=offert_id)
    return render(request, 'offerts/details.html', {'offert' : offert})
