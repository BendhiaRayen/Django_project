from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import VehiculeForm
from .models import Vehicule


def home(request):
    return render(request, 'vehicule/home.html')


class ListeVehicules(ListView):
    model = Vehicule
    template_name = 'vehicule/list.html'
    context_object_name = 'list'
    ordering = ('-created_at',)


class DetailVehicule(DetailView):
    model = Vehicule
    template_name = 'vehicule/detail.html'
    context_object_name = 'detail'


class DeleteVehicule(DeleteView):
    model = Vehicule
    template_name = 'vehicule/delete.html'
    success_url = reverse_lazy('Vehicule:list_class')


class CreateVehicule(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'vehicule/create.html'
    success_url = reverse_lazy('Vehicule:list_class')


class UpdateVehicule(UpdateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = 'vehicule/update.html'
    success_url = reverse_lazy('Vehicule:list_class')
