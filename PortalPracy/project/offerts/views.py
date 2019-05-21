from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Offert, Application
from .forms import ApplicationForm

def home(request):
    offerts = Offert.objects.all().order_by('-publication_date')[:3]
    return render(request, 'home.html', {'offerts': offerts})

class OffertListView(ListView):
    model = Offert
    template_name = 'offerts/offert_list.html' # default: <app>/<model>_<viewtype>.html
    context_object_name = 'offerts'
    ordering = ['-publication_date'] # '-' -> from newest to oldest
    paginate_by = 4

class OffertDetailView(DetailView):
    model = Offert
    template_name = 'offerts/offert_details.html'
    context_object_name = 'offert'

class OffertCreateView(LoginRequiredMixin, CreateView):
    model = Offert
    fields = [  'position',
                'agency',
                'remote',
                'salary_type',
                'min_salary',
                'max_salary',
                'must_have',
                'nice_to_have',
                'duties',
                'benefits',
                'about'
    ]

    template_name = "offerts/add_offert.html"

#nie usuwac tego:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def ApplicationFormCreateView(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid(request.POST):
            form.save()
            return redirect('offerts/application_form')
    return render(request, 'offerts/create_application_form.html', {})

def ApplyView(request, **kwargs):
    return render(request, 'offerts/apply.html')

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    fields = [  'first_name',
                'last_name',
                'email',
                'portfolio_link',
                'message',
    ]
    template_name = "offerts/create_application_form.html"
#nie usuwac tego:
    def form_valid(self, form):
        form.instance.applicant = self.request.user
        offert_id = self.kwargs['pk']
        form.instance.offert = Offert.objects.get(id=offert_id)
        #form.instance.offert = Offert.objects.get(self.kwargs['pk'])
        return super().form_valid(form)
