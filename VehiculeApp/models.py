from django.db import models

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20,unique=True)
    type_vehicule = models.CharField(max_length=20,choices=[('c','camionnette'),
                                                            ('f','fourgon'),
                                                            ('cp','camion porteur'),
                                                            ('sr','semi-remorque')])
    capacite_kg = models.PositiveIntegerField()
    disponibilite = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='vehicules')
