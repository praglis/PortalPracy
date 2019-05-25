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
        return super().is_valid()
'''
def get_answer_set(POST_data, answers):


    class AnswerSet(forms.Form):
        class Meta:
            fields = answers

        def save(self):
            pass
            #write answers into model
    return AnswerSet(POST_data)
'''

class AnswerField(forms.Form):
    possible_answer = forms.CharField(max_length=500)
    class Meta:
        fields = ['possible_answer']
