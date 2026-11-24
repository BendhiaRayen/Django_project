from django.contrib.auth.forms import UserCreationForm

from EntrepriseApp.models import Utilisateur

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = UserCreationForm.Meta.fields + ('email','first_name', 'last_name', 'telephone', 'role', )
        