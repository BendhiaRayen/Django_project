import django.core.validators
from django.db import migrations, models


def assign_registration_codes(apps, schema_editor):
    Utilisateur = apps.get_model('EntrepriseApp', 'Utilisateur')
    counters = {}

    for user in Utilisateur.objects.order_by('created_at', 'user_id'):
        year = user.created_at.strftime('%y')
        number = counters.get(year, 0)

        if number > 99:
            raise RuntimeError(
                f'Impossible de créer plus de 100 codes utilisateur pour l\'année {year}.'
            )

        user.registration_code = f'{year}user{number:02d}'
        user.save(update_fields=['registration_code'])
        counters[year] = number + 1


class Migration(migrations.Migration):

    dependencies = [
        ('EntrepriseApp', '0004_alter_entreprise_matricule_fiscale'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='registration_code',
            field=models.CharField(
                editable=False,
                max_length=8,
                null=True,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message='Le code doit respecter le format AAuserNN.',
                        regex='^\\d{2}user\\d{2}$',
                    )
                ],
            ),
        ),
        migrations.RunPython(
            assign_registration_codes,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='registration_code',
            field=models.CharField(
                editable=False,
                max_length=8,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message='Le code doit respecter le format AAuserNN.',
                        regex='^\\d{2}user\\d{2}$',
                    )
                ],
            ),
        ),
    ]
