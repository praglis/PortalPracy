from django import forms
from offerts.models import Offert

class OffertUpdateForm(forms.ModelForm):
     class Meta:
         model = Offert
         fields = [
            'position',
            'agency',
            'min_salary',
            'max_salary',
            'must_have',
            'nice_to_have',
            'duties',
            'benefits'
        ]

     def is_valid(self, request):
         self.instance.author = request.user
         return super().is_valid()

     def test_func(self):
         offert = self.get_object()
         if self.request.user == offert.author:
             return True
         return False
