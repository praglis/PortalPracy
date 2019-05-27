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

    def is_valid(self, request=None):
        new_offert_id = request.session.get('new_offert_id')
        self.instance.offert = Offert.objects.get(id=new_offert_id)
        request.session['new_question_id'] = self.instance.id
        return super().is_valid()

    def save(self, answers=None):
        print('ApplicationForm.save()')
        if not answers == None:
            print('>>> there are answers')
            self.instance.answer_choices = ""
            for i in range(1, len(answers.fields)+1):
                print(f'type(self.instance.answer_choices): {type(self.instance.answer_choices)}')
                print(f'type(answers.cleaned_data.get(Answer 1)): {type(answers.cleaned_data.get("Answer 1"))}')
                self.instance.answer_choices += answers.cleaned_data.get('Answer %s' % i) + "|"
        print(">>> there are't any answers")
        return super().save()
'''
class AnswerField(forms.Form):
    answer = forms.CharField(max_length=500)
    class Meta:
        fields = ['answer']
'''
class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field_count = kwargs.pop('field_count')
        super(AnswerForm, self).__init__(*args, **kwargs)
        print("init AnswerForm")
        for i in range(1, int(field_count) + 1):
            self.fields['Answer %s' % i] = forms.CharField(max_length=500)
