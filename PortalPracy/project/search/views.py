from django.shortcuts import render
from django.http import HttpResponse
from offerts.models import Offert, Agency, Tag

def is_valid_query(param):
    return param != '' and param is not None

def index(request):
    qs = Offert.objects.all() # qs -> queryset
    tag_set = Tag.objects.all()

    position = request.GET.get('position_name')
    location = request.GET.get('location_name')
    pub_date_min = request.GET.get('pub_date_min')
    pub_date_max= request.GET.get('pub_date_max')
    min_pay= request.GET.get('pay_min')
    tag = request.GET.get('tags')
    remote = request.GET.get('remoteCheck')
    per_hour = request.GET.get('per_hour');
    monthly = request.GET.get('monthly');

    if is_valid_query(position):
        qs = qs.filter(position__icontains=position)

    if is_valid_query(location):
        qs = qs.filter(agency__location__icontains = location)

    if is_valid_query(min_pay):
        qs = qs.filter(min_salary__gte = min_pay) #gte - greater than or equal

    if is_valid_query(pub_date_min):
        qs = qs.filter(publication_date__gte = pub_date_min)

    if is_valid_query(pub_date_max):
        qs = qs.filter(publication_date__lte = pub_date_max)

    if is_valid_query(tag) and tag != "Choose...":
        qs = qs.filter(must_have__name = tag)

    if remote == 'on':
        qs = qs.filter(remote = True)

    if per_hour == 'on':
        qs = qs.filter(salary_type = 'H')

    elif monthly == 'monthly':
        qs = qs.filter(salary_type = 'M')

    context = {
        'queryset' : qs,
        'tag_set' : tag_set
    }
    return render(request, 'search/search.html', context)
