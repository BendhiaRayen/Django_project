from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20,unique=True)
    type_vehicule = models.CharField(max_length=20,choices=[('c','camionnette'),
                                                            ('f','fourgon'),
                                                            ('cp','camion porteur'),
                                                            ('sr','semi-remorque')])
    capacite_kg = models.PositiveIntegerField(validators=[
        MinValueValidator(1,"La capacité doit être supérieure à 0")])
    disponibilite = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='vehicules')

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 't':
            raise ValidationError("Le véhicule doit appartenir à un transporteur.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
