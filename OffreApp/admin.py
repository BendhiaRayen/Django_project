from django.contrib import admin

from OffreApp.models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('expedition', 'transporteur', 'vehicule', 'prix', 'delai_jours', 'statut')
    search_fields = ('expedition__references', 'vehicule__immatriculation')
    list_filter = ('statut',)
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
