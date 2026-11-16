from django.urls import path

from .views import CreateVehicule, DeleteVehicule, DetailVehicule, ListeVehicules, UpdateVehicule, home

app_name = 'Vehicule'

urlpatterns = [
    path('home/', home, name='home'),
    path('list/', ListeVehicules.as_view(), name='list_class'),
    path('detail/<int:pk>/', DetailVehicule.as_view(), name='detail_class'),
    path('delete/<int:pk>/', DeleteVehicule.as_view(), name='delete_class'),
    path('create/', CreateVehicule.as_view(), name='create_vehicule'),
    path('update/<int:pk>/', UpdateVehicule.as_view(), name='update_vehicule'),
]
