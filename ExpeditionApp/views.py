from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from ExpeditionApp.forms import ExpeditionForm
from .models import Expedition
# Create your views here.
def home(request):
    return render(request, 'expedition/home.html')
def welcome(request,name):
    return HttpResponse(f"Welcome, {name}!")
def listExpeditions(request):
    list=Expedition.objects.filter(status='p').order_by('-created_at')
    return render(request, 'expedition/list.html', {'list': list})

def detailExpedition(request, references):
    details = Expedition.objects.get(references=references)
    return render(request, 'expedition/detail.html', {'detail': details})

def deleteExpedition(request, references):
    choix = Expedition.objects.get(references=references)
    choix.delete()
    return render(request, 'expedition/delete.html', {'choix': choix})
class liste_expeditions(ListView):
    model = Expedition
    template_name = 'expedition/list.html'
    context_object_name = 'list'
class detail_expedition(DetailView):
    model = Expedition
    template_name = 'expedition/detail.html'
    context_object_name = 'detail'
class delete_expedition(DeleteView):
    model = Expedition
    template_name = 'expedition/delete.html'
    success_url = reverse_lazy('Expedition:list_class')
class CreateExpeditionView(CreateView):
    model = Expedition
    template_name = 'expedition/create.html'
    #fields = '__all__'
    form_class = ExpeditionForm
    success_url = reverse_lazy('Expedition:list_class')
class UpdateExpeditionView(UpdateView):
    model = Expedition
    template_name = 'expedition/update.html'
    form_class = ExpeditionForm
    success_url = reverse_lazy('Expedition:list_class')
    
    
