from django import forms

from .models import CustomQuestion

class ApplicationForm(forms.ModelForm):
    #question = forms.CharField(max_length = 500)
    class Meta:
        model = CustomQuestion
        fields = ['question', 'answer_type']

    def is_valid(self):
        form.instance.offert = request.session.get('new_offert_id')
        return super().is_valid(form)
