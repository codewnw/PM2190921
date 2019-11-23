from django.shortcuts import render
from first_app.models import Category, SubCategory, Item
from first_app.forms import RegistrationForm

# Create your views here.
def index(request):
    dict = {'items': Item.objects.all(),}
    return render(request, 'first_app/index.html', context=dict)

def registration_view(request):
    form = RegistrationForm()
    return render(request, 'first_app/registration.html', {'form': form})
