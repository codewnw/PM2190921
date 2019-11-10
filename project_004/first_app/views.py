from django.shortcuts import render

# Create your views here.
def index(request):
    msg_dict = {'msg':'This message is from Django application first_app.'}
    return render(request, 'first_app/index.html', context=msg_dict)
