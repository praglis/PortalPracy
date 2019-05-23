from django import forms

from .models import CustomQuestion, Offert

class ApplicationForm(forms.ModelForm):
    answer_count = forms.IntegerField(label='Number of answers:');
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
        return super().is_valid()
