from django.shortcuts import render
from customer.forms import UserForm, CustomerForm

def index(request):
    dict = {'django_title': 'Django web framework for perfactionist.'}
    return render(request, 'customer/index.html', dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        customer_form = CustomerForm(data = request.POST)
        registered = True
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, 'customer/registration.html', {'user_form': user_form, 
    'customer_form': customer_form, 'registered': registered})

def login(request):
    return render(request, 'customer/login.html', {})
