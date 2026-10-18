from django.contrib import admin


from ExpeditionApp.models import Expedition


@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('references', 'ville_depart', 'ville_arrivee', 'date_souhaitee', 'status', 'entreprise')
    search_fields = ('references', 'ville_depart', 'ville_arrivee')
    list_filter = ('status', 'date_souhaitee')
    readonly_fields = ('references', 'created_at', 'updated_at')
    fieldsets = (
        ('Expedition', {
            'fields': ('references', 'ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'description')
        }),
        ('Statut et rattachement', {
            'fields': ('status', 'entreprise')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
