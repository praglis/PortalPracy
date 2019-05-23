from django import forms

from .models import CustomQuestion, Offert

class ApplicationForm(forms.ModelForm):
    #question = forms.CharField(max_length = 500)
    class Meta:
        model = CustomQuestion
        fields = ['question', 'answer_type']

    def is_valid(self, request):
        offert_id = request.session.get('new_offert_id')
        self.instance.offert = Offert.objects.get(id=offert_id)
        return super().is_valid()
