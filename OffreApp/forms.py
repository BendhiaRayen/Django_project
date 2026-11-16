from django import forms

from EntrepriseApp.models import Entreprise
from ExpeditionApp.models import Expedition
from VehiculeApp.models import Vehicule
from .models import Offre


class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ('prix', 'delai_jours', 'statut', 'expedition', 'transporteur', 'vehicule')
        widgets = {
            'prix': forms.NumberInput(attrs={'placeholder': 'Exemple : 850.00', 'min': '0.01', 'step': '0.01'}),
            'delai_jours': forms.NumberInput(attrs={'placeholder': 'Exemple : 3', 'min': '1', 'step': '1'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expedition'].queryset = Expedition.objects.filter(status='p').order_by('-created_at')
        self.fields['expedition'].empty_label = 'Sélectionnez une expédition publiée'
        self.fields['transporteur'].queryset = Entreprise.objects.filter(type_entreprise='t').order_by('raison_sociale')
        self.fields['transporteur'].empty_label = 'Sélectionnez un transporteur'
        vehicle_queryset = Vehicule.objects.filter(disponibilite=True)
        if self.instance and self.instance.pk and self.instance.vehicule_id:
            vehicle_queryset = Vehicule.objects.filter(pk=self.instance.vehicule_id) | vehicle_queryset
        self.fields['vehicule'].queryset = vehicle_queryset.select_related('entreprise').order_by('immatriculation').distinct()
        self.fields['vehicule'].empty_label = 'Sélectionnez un véhicule disponible'
