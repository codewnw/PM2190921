from django.shortcuts import render
from django.views.generic import ListView
from career.models import (Job)

class JobList(ListView):
    model = Job
