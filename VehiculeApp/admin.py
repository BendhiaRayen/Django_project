from django.contrib import admin


from VehiculeApp.models import Vehicule
@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
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
# Register your models here.
#admin.site.register(Vehicule)