from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from offerts.models import Offert
from django.contrib.auth.mixins import LoginRequiredMixin

def form(request):
    return render(request, 'add/form.html')

def apply(request):
    return render(request, 'add/apply.html')

class OffertCreateView(LoginRequiredMixin, CreateView):
    model = Offert
    fields = ['position', 'agency', 'min_salary', 'max_salary', 'must_have', 'nice_to_have', 'duties', 'benefits']
    template_name = "add/offert.html"
#nie usuwac tego:
    #def form_valid(self, form):
        #form.instance.author = self.request.user
        #return super().form_valid(form)
