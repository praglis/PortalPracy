from django import forms

from .models import CustomQuestion, Offert

class ApplicationForm(forms.ModelForm):
    #self.fields['question'].label ='Your question:'
    #self.fields['answer_type'].label = 'Choose the type of answer you would like to get:'
    class Meta:
        model = CustomQuestion
        fields = ['question', 'answer_type']
        labels = {
            "question": "Your question:",
            "answer_type": "Choose the type of answer you would like to get:"
        }

    def is_valid(self, request):
        offert_id = request.session.get('new_offert_id')
        self.instance.offert = Offert.objects.get(id=offert_id)
        return super().is_valid()
