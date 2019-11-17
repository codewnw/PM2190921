from django.shortcuts import render
from first_app.models import Category, SubCategory, Item

# Create your views here.
def index(request):
    dict = {
        'heading': 'Welcome to Django',
        'paragraph': 'Django is high level web framework for perfectionist with deadlines.',
        'item': Item.objects.all()[0],
    }
    return render(request, 'first_app/index.html', context=dict)
