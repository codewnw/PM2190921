from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'index.html'

class LoggedOutView(LoginRequiredMixin, TemplateView):
    template_name = 'logout.html'

class ContactUsView(TemplateView):
    template_name = 'contact_us.html'