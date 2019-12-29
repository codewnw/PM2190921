from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from customer.forms import UserForm, CustomerForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    dict = {'django_title': 'Django web framework for perfactionist.'}
    return render(request, 'customer/index.html', dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        customer_form = CustomerForm(data = request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            registered = True
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, 'customer/registration.html', {'user_form': user_form, 
    'customer_form': customer_form, 'registered': registered})

def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is not active.')
        else:
            print('Login failed for username (username) and password (password)')
            return HttpResponse("Invalid credentials.")
    return render(request, 'customer/login.html', {})

@login_required
def customer_logout(request):
    print('here')
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def secrete_message(request):
    return HttpResponse('Merry Cristmas!!!')