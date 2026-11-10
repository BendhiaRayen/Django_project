
from django.urls import path

from ExpeditionApp.views import CreateExpeditionView, UpdateExpeditionView, delete_expedition, deleteExpedition, detail_expedition, detailExpedition, home, listExpeditions, liste_expeditions, welcome

app_name = 'Expedition'

urlpatterns = [
    path('home/', home, name='home'),
    path('welcome/<str:name>/', welcome, name='welcome'),
    path('list/', listExpeditions, name='list_expeditions'),  # Add this line to include the listExpeditions view
    path('detail/<str:references>/', detailExpedition, name='detail'),
    path('delete/<str:references>/', deleteExpedition, name='delete'),
    path('list1/', liste_expeditions.as_view(), name='list_class'),
    path('detail1/<int:pk>/', detail_expedition.as_view(), name='detail_class'),
    path('delete1/<int:pk>/', delete_expedition.as_view(), name='delete_class'),
    path('create/', CreateExpeditionView.as_view(), name='create_expedition'),
    path('update/<int:pk>/', UpdateExpeditionView.as_view(), name='update_expedition')
    ]
