from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    feedback = forms.CharField(widget = forms.Textarea)
