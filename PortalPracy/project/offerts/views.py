from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import json

from .models import Offert, Application, CustomQuestion
from .forms import ApplicationForm, AnswerForm

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
        #form = ApplicationForm(request.POST)
        if not request.POST.get('answer_type') == 'T':
            ##request.session['new_question'] = json.dumps(form)
            return redirect('offerts:set_answers')
        #if form.is_valid(request=request):
            #if form.save().answer_type != 'T':
                #request.session['answer_count'] = form.cleaned_data.get('answer_count')
                #request.session['new_question_id'] = form.instance.id
                #print('answer_count in AFCV:', request.session['answer_count'])
                #print('new_question_id in AFCV:', request.session['new_question_id'])
                #return redirect('offerts:set_answers')
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
    print("AAV00 json:", request.session['new_question'])
    question = json.loads(request.session['new_question'])
    #answer_count = request.session.get('answer_count')
    answer_count = question.get('answer_count')
    print("AAV01 answer_count:", answer_count)
    if request.method == "POST":
        #question_id = request.session.get('new_question_id')
        #question = CustomQuestion.objects.get(id=question_id)
        question_form = ApplicationForm(question)
        answer_form = AnswerForm(request.POST, field_count=answer_count)
        print("prevalid")
        if answer_form.is_valid() and question_form.is_valid(request=request):
            print('is_valid')
            question_form.save(answers=answer_form)
    else:
        answer_form = AnswerForm(field_count=answer_count)
        print("answer_count in AAV:", answer_count)
    context = {
        #'answer_count' : answer_count,
        'form' : answer_form
    }
    return render(request, 'offerts/application_answers.html', context)

'''
@login_required
def ApplicationAnswersView(request, answer_count=0, question_id=0):
    set = []

    if request.method == "POST":
        question = CustomQuestion.objects.get(id=question_id)
        form = ApplicationForm(instance=question)

        for answer in answer_count:
            set.append(AnswerField(request.POST))
        print('between forr')
        for answer in answer_count:
            if set[answer].is_valid():
                print('is_valid')
                form.save(set[answer])
            else: all_valid = False

        if all_valid:
            print('all answers valid, exitting ApllicationAnswersView')
            redirect(ApplicationFormCreateView())
    else:
        for answer in answer_count:
            set.append(AnswerField())
    context = {
        'answer_count' : answer_count,
        'form' : set
    }
    # CustomQuestion.objects.filter(pk=some_value).update(answer_choices='some value')
    return render(request, 'offerts/application_answers.html', context)
'''

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
