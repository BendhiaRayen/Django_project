from django import forms

from EntrepriseApp.models import Entreprise
from .models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponibilite', 'entreprise')
        widgets = {
            'immatriculation': forms.TextInput(attrs={'placeholder': 'Exemple : 123 تونس 4567'}),
            'capacite_kg': forms.NumberInput(attrs={'placeholder': 'Exemple : 3500', 'min': '1', 'step': '1'}),
            'disponibilite': forms.CheckboxInput(attrs={'style': 'width:auto;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['entreprise'].queryset = Entreprise.objects.filter(type_entreprise='t').order_by('raison_sociale')
        self.fields['entreprise'].empty_label = 'Sélectionnez un transporteur'
