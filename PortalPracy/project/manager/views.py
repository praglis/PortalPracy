from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from offerts.models import Offert, Application

class MyOffertsListView(ListView):
     model = Offert
     template_name = 'manager/my_offerts.html' # default: <app>/<model>_<viewtype>.html
     context_object_name = 'offerts'
     ordering = ['-publication_date'] # '-' -> from newest to oldest

     def get_queryset(self):
         return Offert.objects.filter(author=self.request.user).order_by('-publication_date')


class RepliesListView(ListView):
     model = Application
     template_name = 'manager/replies.html' # default: <app>/<model>_<viewtype>.html
     context_object_name = 'applications'
     #ordering = ['-publication_date'] # '-' -> from newest to oldest
     #def get_context_data(self, **kwargs): -> zwrocic context: aplikacje i odpowiadajace im profile uzytkownikow i oferty
     def get_queryset(self):
         applications = Application.objects.all().filter(offert_id=self.kwargs['pk'])
         return applications

class OffertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = Offert
     fields = ['position', 'agency', 'min_salary', 'max_salary', 'must_have', 'nice_to_have', 'duties', 'benefits']
     template_name = "manager/offert_update.html"

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

     def test_func(self):
         offert = self.get_object()
         if self.request.user == offert.author:
             return True
         return False


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
