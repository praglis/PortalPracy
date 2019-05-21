from django import forms
from .models import CustomQuestion

class ApplicationForm(forms.ModelForm):
    #question = forms.CharField(max_length = 500)
    class Meta:
        model = CustomQuestion
        fields = ['question']

    def is_valid(self, data):
        super().is_valid()
        question = data.get('question')
