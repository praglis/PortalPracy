from django.shortcuts import render
from django.http import HttpResponse
from offerts.models import Offert, Agency

def index(request):
    qs = Offert.objects.all()
    ag = Agency.objects.all()

    position_query = request.GET.get('position_name')
    location = request.GET.get('location_name')
    pub_date_min = request.GET.get('pub_date_min')
    pub_date_max= request.GET.get('pub_date_max')
    min_pay= request.GET.get('pay_min')
    tags = request.GET.get('tags')

    if position_query != '' and position_query is not None:
        qs = qs.filter(position__icontains=position_query)

    if location != '' and location is not None:
        qs = qs.filter(agency__location__icontains = location)

    context = {
        'queryset' : qs
    }
    return render(request, 'search/index.html', context)
