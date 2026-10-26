from django.contrib import admin


from VehiculeApp.models import Vehicule
@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = (
    'immatriculation',
    'capacite_kg',
    'created_at',
    'disponibilite',
     )
    search_fields = ('immatriculation', 'type_vehicule')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identification', {
            'fields': ('immatriculation', 'type_vehicule', 'capacite_kg')
        }),
        ('Statut et rattachement', {
            'fields': ('disponibilite', 'entreprise')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
  
#admin.site.register(Vehicule)