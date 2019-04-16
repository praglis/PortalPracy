from django import forms

class ApplicationForm(forms.Form):
    motivation = forms.TextField(label='Why you want to work there?')
    
