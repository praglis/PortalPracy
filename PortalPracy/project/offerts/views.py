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
                answer_count = form.cleaned_data.get('answer_count')
                return ApplicationAnswersView(request, answer_count=range(answer_count), previous_view_request=request)
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


@login_required
def ApplicationAnswersView(request, answer_count=0, previous_view_request=None):
    set = []
    if not previous_view_request:
        request.session['new_question_id'] = previous_view_request.session.get('new_question_id')

    if request.method == "POST":
        question_id = request.session.get('new_question_id')
        question = CustomQuestion.objects.get(id=question_id)
        form = ApplicationForm(instance=question)

        for answer in answer_count:
            set.append(AnswerField(request.POST))

        for answer in answer_count:
            if set.is_valid():
                form.add_answer(set[answer])
            else: all_valid = False

        if all_valid:
            redirect(ApplicationFormCreateView())
    else:
        for answer in answer_count:
            set.append(AnswerField())
    context = {
        'answer_count' : answer_count,
        'form' : set
    }
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
