from django.shortcuts import render
from first_app.models import Category, SubCategory, Item
from first_app.forms import *

# Create your views here.
def index(request):
    dict = {'items': Item.objects.all(),}
    return render(request, 'first_app/index.html', context=dict)

def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Feedback: ' + form.cleaned_data['feedback'])
            return render(request, 'first_app/login.html', {})
    return render(request, 'first_app/registration.html', {'form': form})

def item_view(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category']
            sub_category_name = form.cleaned_data['sub_category']
            category = Category.objects.get(name = category_name)
            sub_category = SubCategory.objects.get(name = sub_category_name)
            print(category)
            print(sub_category)
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            item = Item(category = category,
            sub_category = sub_category,
            name = name,
            description = description,
            image = image)
            print(item)
            item.save()
            dict = {'items': Item.objects.all(),}
            return render(request, 'first_app/index.html', context=dict)
    return render(request, 'first_app/item_form.html', {'form': form})
