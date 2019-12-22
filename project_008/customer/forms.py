from django import forms
from django.contrib.auth.models import User
from customer.models import Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('portfolio', 'picture')