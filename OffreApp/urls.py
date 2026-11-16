from django.urls import path

from .views import CreateOffre, DeleteOffre, DetailOffre, ListeOffres, UpdateOffre, home

app_name = 'Offre'

urlpatterns = [
    path('home/', home, name='home'),
    path('list/', ListeOffres.as_view(), name='list_class'),
    path('detail/<int:pk>/', DetailOffre.as_view(), name='detail_class'),
    path('delete/<int:pk>/', DeleteOffre.as_view(), name='delete_class'),
    path('create/', CreateOffre.as_view(), name='create_offre'),
    path('update/<int:pk>/', UpdateOffre.as_view(), name='update_offre'),
]
