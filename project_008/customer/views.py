from django.shortcuts import render

def index(request):
    dict = {'django_title': 'Django web framework for perfactionist.'}
    return render(request, 'customer/index.html', dict)

def register(request):
    return render(request, 'customer/registration.html', {})

def login(request):
    return render(request, 'customer/login.html', {})
