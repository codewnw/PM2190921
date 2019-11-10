from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {
        'heading': 'Welcome to Django',
        'paragraph': 'Django is high level web framework for perfectionist with deadlines.'
    }
    return render(request, 'first_app/index.html', context=dict)
