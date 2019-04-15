from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from offerts.models import Offert

class MyOffertsListView(ListView):
     model = Offert
     template_name = 'manager/my_offerts.html' # default: <app>/<model>_<viewtype>.html
     context_object_name = 'offerts'
     ordering = ['-publication_date'] # '-' -> from newest to oldest
 # http://localhost:8000/offerts/update/10/
 # class OffertUpdateView(LoginRequiredMixin, UserPassesTestMixin UpdateView):
class OffertUpdateView(LoginRequiredMixin, UpdateView):
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

 # class OffertUpdateView(LoginRequiredMixin, UserPassesTestMixin UpdateView):
class OffertDeleteView(LoginRequiredMixin, DeleteView):
     model = Offert
     success_url = '/offerts/'
     template_name = "manager/offert_confirm_delete.html"

     def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

     def test_func(self):
         offert = self.get_object()
         if self.request.user == offert.author:
             return True
         return False
