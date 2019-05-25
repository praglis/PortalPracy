from django import forms

from .models import CustomQuestion, Offert

class ApplicationForm(forms.ModelForm):
    answer_count = forms.IntegerField(label='Number of answers:', initial=3);
    class Meta:
        model = CustomQuestion
        fields = ['question', 'answer_type', 'answer_count']
        labels = {
            "question": "Your question:",
            "answer_type": "Answer type:"
        }

    def is_valid(self, request):
        offert_id = request.session.get('new_offert_id')
        self.instance.offert = Offert.objects.get(id=offert_id)
        request.session['new_question_id'] = self.instance.id
        return super().is_valid()

    def save(self, answer=None):
        if answer:
            self.instance.answer_choices += answer.cleaned_data.get('answer')
        return super().save()

class AnswerField(forms.Form):
    answer = forms.CharField(max_length=500)
    class Meta:
        fields = ['answer']
