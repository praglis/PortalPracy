from django import forms
from offerts.models import Offert

class OffertUpdateForm(forms.ModelForm):
     class Meta:
         model = Offert
         fields = [
            'position',
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

     def is_valid(self, request):
         self.instance.author = request.user
         return super().is_valid()
