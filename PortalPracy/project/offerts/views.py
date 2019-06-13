from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import json

from .models import Offert, Application, CustomQuestion, CustomAnswer
from sign_in.models import Profile
from .forms import ApplicationForm, AnswerForm, ApplyForm

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
        request.session['new_question'] = json.dumps(request.POST)
        if not request.POST.get('answer_type') == 'T':
            return redirect('offerts:set_answers')
        else:
            form = ApplicationForm(request.POST)
            if form.is_valid(request=request):
                form.save()
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
def ApplicationAnswersView(request):
    question = json.loads(request.session['new_question'])
    answer_count = question.get('answer_count')
    if request.method == "POST":
        question_form = ApplicationForm(question)
        answer_form = AnswerForm(request.POST, field_count=answer_count)
        if answer_form.is_valid() and question_form.is_valid(request=request):
            question_form.save(answers=answer_form)
            return redirect('offerts:application_form')
    else:
        answer_form = AnswerForm(field_count=answer_count)
    context = {
        'form' : answer_form
    }
    return render(request, 'offerts/application_answers.html', context)

@login_required
def ApplyView(request, **kwargs):
    offert_id = kwargs['pk']
    offert = Offert.objects.get(id=offert_id)
    questions = CustomQuestion.objects.filter(offert=offert)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid(request, offert_id):
            for question in questions:
                if question.answer_type == 'T':
                    answer = 'lalala'
                custom_answer = CustomAnswer.objects.create(
                    applicant =     request.user,
                    question =      question,
                    answer_type =   question.answer_type,
                    answer =        answer)
            form.save()
            return redirect('home')

        print("form.errors: " + str(form.errors))
        print("cv: " + str(form.clean()))

    else:
        profile = Profile.objects.get(user=request.user)
        form = ApplyForm()

    context = {
        'form' : form,
        'offert' : offert,
        'questions' : questions
    }
    return render(request, 'offerts/apply.html', context)

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
