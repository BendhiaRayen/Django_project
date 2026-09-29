from django.db import models
class Offre(models.Model):
    prix = models.DecimalField()
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(max_length=20, choices=[
        ('p','proposee'),
        ('a','acceptee'),
        ('r','refusee'),
        ('re','retiree')])
    date_proposition = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expedition = models.ForeignKey('ExpeditionApp.Expedition', on_delete=models.CASCADE, related_name='offres')
    transporteur = models.ForeignKey('EntrepriseApp', on_delete=models.CASCADE, related_name='offres_transport')
    vehicule = models.ForeignKey('VehiculeApp.Vehicule', on_delete=models.CASCADE, null=True)


