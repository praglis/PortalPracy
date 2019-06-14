from django.views.generic import ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy, resolve

#from django.contrib.auth.models import User
from offerts.models import Offert, Application, CustomAnswer
from .forms import OffertUpdateForm

class MyOffertsListView(ListView):
     model = Offert
     template_name = 'manager/my_offerts.html' # default: <app>/<model>_<viewtype>.html
     context_object_name = 'offerts'
     ordering = ['-publication_date'] # '-' -> from newest to oldest

     def get_queryset(self):
         return Offert.objects.filter(author=self.request.user).order_by('-publication_date')

def RepliesView(request, **kwargs):

    applications = Application.objects.all().filter(offert_id=kwargs['pk'])

    context = {
    'applications' : applications
    }
    return render(request,'manager/replies.html',context)

def ReplyDetails(request, **kwargs):
    application = Application.objects.all().get(id=kwargs['pk'])
    custom_answers =  CustomAnswer.objects.all().filter(application=application)
    context = {
    'application' : application,
    'custom_answers' : custom_answers
    }
    return render(request,'manager/reply_details.html',context)

@login_required
def OffertUpdateView(request, **kwargs):
    my_offert = Offert.objects.get(id=kwargs['pk'])

    if request.method == 'POST':
        form = OffertUpdateForm(request.POST, instance=my_offert)

        if form.is_valid(request):
            form.save()
            return redirect('/manage/user/<request.user>/')

    else:
        form = OffertUpdateForm(instance=my_offert)

    context = { 'form' : form }
    return render(request, "manager/offert_update.html", context)


class OffertDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
     model = Offert
     success_url = '/manage/user/<str:username>/'
     template_name = "manager/offert_confirm_delete.html"

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

     def test_func(self):
         offert = self.get_object()
         if self.request.user == offert.author:
             return True
         return False
