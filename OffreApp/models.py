from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2,validators=[
        MinValueValidator(0.01,"Le prix doit être supérieur à 0.")])
    delai_jours = models.PositiveIntegerField(validators=[
        MinValueValidator(1,"Le délai doit être au moins de 1 jour.")])
    statut = models.CharField(max_length=20, choices=[
        ('p','proposee'),
        ('a','acceptee'),
        ('r','refusee'),
        ('re','retiree')],default='p')
    date_proposition = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expedition = models.ForeignKey('ExpeditionApp.Expedition', on_delete=models.CASCADE, related_name='offres')
    transporteur = models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='offres_transport')
    vehicule = models.ForeignKey('VehiculeApp.Vehicule', on_delete=models.CASCADE, related_name='offres_vehicule')

    def clean(self):
        super().clean()
        if self.transporteur_id and self.transporteur.type_entreprise != 't':
            raise ValidationError("Seuls les transporteurs peuvent créer des offres.")
        if self.vehicule_id and self.transporteur_id:
            if self.vehicule.entreprise_id != self.transporteur_id:
                raise ValidationError("Le véhicule doit appartenir au transporteur de l'offre.")
        if self._state.adding:
            if self.expedition_id and self.expedition.status != 'p':
                raise ValidationError("L'expédition doit être publiée pour recevoir une nouvelle offre.")
            if self.vehicule_id and not self.vehicule.disponibilite:
                raise ValidationError("Le véhicule doit être disponible pour une nouvelle offre.")
        if self.statut == 'p' and self.expedition_id and self.transporteur_id:
            offres = Offre.objects.filter(expedition=self.expedition,transporteur=self.transporteur,statut='p').exclude(pk=self.pk)
            if offres.exists():
                raise ValidationError("Une offre proposée existe déjà pour cette expédition et ce transporteur.")
        if self.vehicule_id and self.expedition_id:
            if self.expedition.poids_kg > self.vehicule.capacite_kg:
                raise ValidationError("Le poids dépasse la capacité du véhicule.")
            if self.vehicule.type_vehicule == 'c' and self.expedition.poids_kg > 1500:
                raise ValidationError("Une camionnette ne peut pas transporter plus de 1500 kg.")
            if self.vehicule.type_vehicule == 'f' and self.expedition.poids_kg > 3500:
                raise ValidationError("Un fourgon ne peut pas transporter plus de 3500 kg.")
            if self.vehicule.type_vehicule == 'cp' and self.expedition.poids_kg > 19000:
                raise ValidationError("Un camion porteur ne peut pas transporter plus de 19000 kg.")
            if self.vehicule.type_vehicule == 'sr' and self.expedition.poids_kg > 26000:
                raise ValidationError("Une semi-remorque ne peut pas transporter plus de 26000 kg.")

    def save(self, *args, **kwargs):
        ancien_statut = None
        if not self._state.adding:
            ancien_statut = Offre.objects.filter(pk=self.pk).values_list('statut',flat=True).first()
        self.full_clean()
        super().save(*args, **kwargs)
        if self.statut == 'a' and ancien_statut != 'a':
            self.expedition.status = 'a'
            self.expedition.save()
            Offre.objects.filter(expedition=self.expedition,statut='p').exclude(pk=self.pk).update(statut='r')


