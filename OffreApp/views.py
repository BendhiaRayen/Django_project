from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import OffreForm
from .models import Offre


def home(request):
    return render(request, 'offre/home.html')


class ListeOffres(ListView):
    model = Offre
    template_name = 'offre/list.html'
    context_object_name = 'list'
    ordering = ('-created_at',)


class DetailOffre(DetailView):
    model = Offre
    template_name = 'offre/detail.html'
    context_object_name = 'detail'


class DeleteOffre(DeleteView):
    model = Offre
    template_name = 'offre/delete.html'
    success_url = reverse_lazy('Offre:list_class')


class CreateOffre(CreateView):
    model = Offre
    form_class = OffreForm
    template_name = 'offre/create.html'
    success_url = reverse_lazy('Offre:list_class')


class UpdateOffre(UpdateView):
    model = Offre
    form_class = OffreForm
    template_name = 'offre/update.html'
    success_url = reverse_lazy('Offre:list_class')
