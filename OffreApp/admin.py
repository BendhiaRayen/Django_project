from django.contrib import admin
import csv
from django.http import HttpResponse
from OffreApp.models import Offre
from django.utils.html import format_html

class PrixFilter(admin.SimpleListFilter):
    title = 'prix'
    parameter_name = 'prix_range'

    def lookups(self, request, model_admin):
        return [
            ('low', 'Moins de 1000'),
            ('medium', '1000 à 10000'),
            ('high', 'Plus de 10000'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(prix__lt=1000)

        if self.value() == 'medium':
            return queryset.filter(
                prix__gte=1000,
                prix__lte=10000,
            )

        if self.value() == 'high':
            return queryset.filter(prix__gt=10000)

        return queryset
@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = (
        'attachment; filename="offres.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        'reference_expedition',
        'transporteur',
        'prix',
        'statut',
    ])

    for offre in queryset.select_related('expedition', 'transporteur'):
        writer.writerow([
            offre.expedition.references,
            offre.transporteur.raison_sociale,
            offre.prix,
            offre.get_statut_display(),
        ])

    return response
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    autocomplete_fields = ('expedition', 'transporteur', 'vehicule')
    list_display = ('expedition', 'transporteur', 'vehicule', 'prix', 'delai_jours', 'statut')
    search_fields = ('expedition__references', 'vehicule__immatriculation')
    list_filter = ('statut', PrixFilter)
    readonly_fields = ('date_proposition', 'created_at', 'updated_at')
    fieldsets = (
        ('Offre', {
            'fields': ('prix', 'delai_jours', 'statut')
        }),
        ('Rattachement', {
            'fields': ('expedition', 'transporteur', 'vehicule')
        }),
        ('Horodatage', {
            'fields': ('date_proposition', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    actions = [exporter_offres_csv]
    def get_readonly_fields(self, request, obj=None):
        base = list(self.readonly_fields)

        if obj and obj.statut == 'a':
            return base + ['prix', 'delai_jours']

        return base
    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'p': '#F0AD4E',
            'a': '#5CB85C',
            'r': '#D9534F',
            're': '#777777',
        }

        return format_html(
            '<span style="background:{}; color:white; '
            'padding:3px 8px; border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999999'),
            obj.get_statut_display(),
        )
    