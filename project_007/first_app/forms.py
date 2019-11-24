from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    feedback = forms.CharField(widget = forms.Textarea, required=False)

class ItemForm(forms.Form):
    category = forms.CharField()
    sub_category = forms.CharField()
    name = forms.CharField()
    description = forms.CharField()
    image = forms.URLField()
