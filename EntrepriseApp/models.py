from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator,RegexValidator
from django.utils import timezone

#validators
def validate_email(value):
    if not value:
        raise ValidationError("L'email ne peut pas être vide.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("L'email doit se terminer par '@gmail.com'.")
matricule_fiscale_validator =RegexValidator(
    regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
    message="Format erroné"
)

class Utilisateur(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    registration_code = models.CharField(
        max_length=8,
        unique=True,
        editable=False,
        validators=[
            RegexValidator(
                regex=r'^\d{2}user\d{2}$',
                message='Le code doit respecter le format AAuserNN.',
            )
        ],
    )
    email = models.EmailField(unique=True, validators=[validate_email])
    telephone = models.CharField(max_length=15,blank=True, null=True)
    role = models.CharField(max_length=20,choices=[
        ('admin','Admin'),
        ('c','Chargeur'),
        ('t','Transporteur')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.registration_code:
            year = timezone.localdate().strftime('%y')
            prefix = f'{year}user'

            last_user = (
                Utilisateur.objects
                .filter(registration_code__startswith=prefix)
                .order_by('-registration_code')
                .first()
            )

            if last_user:
                next_number = int(last_user.registration_code[-2:]) + 1
            else:
                next_number = 0

            if next_number > 99:
                raise ValidationError(
                    f'La limite de 100 utilisateurs pour l\'année {year} est atteinte.'
                )

            self.registration_code = f'{prefix}{next_number:02d}'

        super().save(*args, **kwargs)
    
class Entreprise(models.Model): 
    raison_sociale = models.CharField(max_length=200,blank=False, null=False )
    matricule_fiscale = models.CharField(max_length=17,unique=True, validators=[matricule_fiscale_validator])
    adresse = models.TextField(validators=[
        MinLengthValidator(20,"L'adresse ne peut pas pas avoir moins de 20 caractères"),
        MaxLengthValidator(400,"L'adresse ne peut pas pas avoir plus de 400 caractères")])
    type_entreprise = models.CharField(max_length=100,choices=[
        ('c','Chargeur'),
        ('t','Transporteur')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise')
