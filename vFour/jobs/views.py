from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from jobs.models import (Job)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class JobList(ListView):
    model = Job


class JobDetailView(PermissionRequiredMixin, DetailView):
    model = Job
    permission_required = ('jobs.view_job')