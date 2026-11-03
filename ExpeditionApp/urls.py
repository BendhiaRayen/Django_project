
from django.urls import path

from ExpeditionApp.views import deleteExpedition, detailExpedition, home, listExpeditions, welcome

app_name = 'Expedition'

urlpatterns = [
    path('home/', home, name='home'),
    path('welcome/<str:name>/', welcome, name='welcome'),
    path('list/', listExpeditions, name='list_expeditions'),  # Add this line to include the listExpeditions view
    path('detail/<str:references>/', detailExpedition, name='detail'),
    path('delete/<str:references>/', deleteExpedition, name='delete'),
    ]
