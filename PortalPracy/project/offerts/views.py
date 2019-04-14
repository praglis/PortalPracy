from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Offert, Company, Agency

# class based view
class OffertListView(ListView):
    model = Offert
    template_name = 'offerts/index.html' # default: <app>/<model>_<viewtype>.html
    context_object_name = 'offerts'
    ordering = ['-publication_date'] #from newest to oldest


def details(request, offert_id):
    offert = get_object_or_404(Offert, pk=offert_id)
    context = {'offert' : offert}
    return render(request, 'offerts/details.html', context)
