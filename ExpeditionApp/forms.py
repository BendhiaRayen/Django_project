
from django import forms

from ExpeditionApp.models import Expedition

class ExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields ="__all__"
        exclude = ['references','id','created_at', 'updated_at']