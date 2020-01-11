from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from jobs.models import (Job)


class JobList(ListView):
    model = Job


class JobDetailView(DetailView):
    model = Job
