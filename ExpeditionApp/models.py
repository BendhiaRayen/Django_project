from django.db import models

class Expedition(models.Model):
    references= models.CharField(max_length=100,unique=True)
    ville_depart= models.CharField(max_length=100)
    ville_arrivee= models.CharField(max_length=100)
    poids_kg= models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee= models.DateField()
    description= models.TextField()
    status=models.CharField(max_length=20,choices=[
        ('p','publiee'),
        ('a','attribuee'),
        ('ec','en_cours'),
        ('l','livree'),
        ('ann','annulee')
    ], default='p')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='expeditions')

