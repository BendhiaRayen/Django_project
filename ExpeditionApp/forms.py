
from django import forms

from ExpeditionApp.models import Expedition

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields ="__all__"
        exclude = ['references','id','created_at', 'updated_at']
        widgets = {
            'ville_depart': forms.TextInput(attrs={'placeholder': 'Exemple : Tunis'}),
            'ville_arrivee': forms.TextInput(attrs={'placeholder': 'Exemple : Sfax'}),
            'poids_kg': forms.NumberInput(attrs={'placeholder': 'Exemple : 1250.50', 'min': '0.01', 'step': '0.01'}),
            'date_souhaitee': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Exemple : 12 palettes de pièces automobiles, livraison avant 17h.'}),
        }
