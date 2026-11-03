from django.shortcuts import render
from django.http import HttpResponse
from .models import Expedition
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Expedition App!")
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

    
