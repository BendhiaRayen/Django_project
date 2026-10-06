from datetime import timezone

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
class Expedition(models.Model):
    references= models.CharField(max_length=100,unique=True)
    ville_depart= models.CharField(max_length=100)
    ville_arrivee= models.CharField(max_length=100)
    poids_kg= models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01,"Le poids doit être supérieur à 0")])
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
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'chargeur':
            raise ValidationError("Seuls les chargeurs peuvent créer des expeditions.")
    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime("%Y")
        prefix = f"EXP_{annee}_"
        dernier=cls.objects.filter(references__startswith=prefix).order_by('references').last()
        compteur = int(dernier.references[-5:]) + 1 if dernier else 1
        if compteur > 99999:
            raise ValidationError("Limit exeeded")
        return f"{prefix}{compteur:05d}"
    def save(self, *args, **kwargs):
        if not self.references:
            self.references = self._generate_reference()
        self.full_clean()  # Validate the model before saving
        super().save(*args, **kwargs)