from django import forms
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

from .models import CustomQuestion, Offert, Application

class OffertCreateForm(forms.ModelForm):
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

    def save(self, request):
        self.instance.author = request.user
        saved_data = super().save()
        request.session['new_offert_id'] = self.instance.id
        return saved_data

class ApplicationForm(forms.ModelForm):
    answer_count = forms.IntegerField(label='Number of answers (max. 15):', initial=3);
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
        if not answers == None:
            self.instance.answer_choices = ""
            for i in range(1, len(answers.fields)+1):
                self.instance.answer_choices += answers.cleaned_data.get('Answer %s' % i) + "|"
        return super().save()

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        field_count = kwargs.pop('field_count')
        if int(field_count) > 15:
            field_count = 15
        super(AnswerForm, self).__init__(*args, **kwargs)

        for i in range(1, int(field_count) + 1):
            self.fields['Answer %s' % i] = forms.CharField(max_length=500)

class ApplyForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['email','first_name','last_name','cv','portfolio_link','message']
        labels = {
            "email": "Contact email:",
            "cv": "Your CV:",
            'portfolio_link' : "Link to your portfolio:",
        }

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        self.fields['portfolio_link'].required = False

    def is_valid(self, request, offert_id):

        self.instance.applicant = request.user
        self.instance.offert = Offert.objects.get(id=offert_id)
        try:
            if request.FILES['InMemoryUploadedFile'] == None:
                pass
        except MultiValueDictKeyError:
            self.instance.cv = request.user.profile.cv
        return super().is_valid()
