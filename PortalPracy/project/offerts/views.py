from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Offert, Application, CustomQuestion
from .forms import ApplicationForm, AnswerField

def home(request):
    offerts = Offert.objects.all().order_by('-publication_date')[:3]
    return render(request, 'home.html', {'offerts': offerts})

class OffertListView(ListView):
    model = Offert
    template_name = 'offerts/offert_list.html' # default: <app>/<model>_<viewtype>.html
    context_object_name = 'offerts'
    ordering = ['-publication_date'] # '-' -> from newest to oldest
    paginate_by = 6

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
        saved_data = super().form_valid(form)
        self.request.session['new_offert_id'] = form.instance.id
        return saved_data

@login_required
def ApplicationFormCreateView(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid(request):
            if form.save().answer_type != 'T':
                return ApplicationAnswersView(request, range(form.cleaned_data.get('answer_count')))
    else:
        form = ApplicationForm()

    offert_id = request.session.get('new_offert_id')
    offert = Offert.objects.get(id=offert_id)
    questions = CustomQuestion.objects.filter(offert=offert)

    context = {
        'form': form,
        'questions': questions
    }
    return render(request, 'offerts/create_application_form.html', context)

def ApplicationAnswersView(request, answer_count):
    '''
    answers = []
    for i in answer_count:
        answers.append('answer')
'''
    form = []
    if request.method == "POST":
        for answer in answer_count:
            form.append(AnswerField(request.POST))
        #if form.is_valid():
            #form.save()
    else:
        for answer in answer_count:
            form.append(AnswerField())
    context = {
        'answer_count' : answer_count,
        'form' : form
    }
    # CustomQuestion.objects.filter(pk=some_value).update(answer_choices='some value')
    return render(request, 'offerts/application_answers.html', context)

@login_required
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

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        offert_id = self.kwargs['pk']
        form.instance.offert = Offert.objects.get(id=offert_id)
        #form.instance.offert = Offert.objects.get(self.kwargs['pk'])
        return super().form_valid(form)
