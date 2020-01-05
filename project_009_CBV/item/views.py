from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView, CreateView, UpdateView, DeleteView)
from item.models import (Item)
from django.urls import reverse_lazy


def index(request):
    print('index method view')
    return render(request, 'index.html', {})


class IndexView(View):
    def get(self, request):
        print('IndexView')
        return render(request, 'index.html', {})


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class ContactUsView(TemplateView):
    template_name = 'contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mobile'] = '9876543210'
        return context


class ItemListView(ListView):
    model = Item


class ItemDetailView(DetailView):
    model = Item


class CreateItemView(CreateView):
    model = Item
    fields = ('name', 'description', 'price', 'image')


class UpdateItemView(UpdateView):
    model = Item
    fields = ('name', 'description', 'price', 'image')


class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy('item:list')
