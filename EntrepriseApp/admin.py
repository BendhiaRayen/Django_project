from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from EntrepriseApp.models import Entreprise, Utilisateur
from VehiculeApp.models import Vehicule

admin.site.site_header = "TransConnect — Administration"
admin.site.site_title = "TransConnect"
admin.site.index_title = "Tableau de bord"


class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 0
    fields = (
        'immatriculation',
        'type_vehicule',
        'capacite_kg',
        'disponibilite',
    )
    show_change_link = True
@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    inlines = [VehiculeInline]
    list_display = ('raison_sociale', 'matricule_fiscale', 'type_entreprise', 'gerant')
    search_fields = ('raison_sociale', 'matricule_fiscale', 'gerant__username')
    list_filter = ('type_entreprise',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identification', {
            'fields': ('raison_sociale', 'matricule_fiscale', 'adresse')
        }),
        ('Type et gerant', {
            'fields': ('type_entreprise', 'gerant')
        }),
        ('Horodatage', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


class UserAdmin(DjangoUserAdmin):
    list_display = (
        'user_id',
        'username',
        'email',
        'telephone',
        'role',
        'is_active',
    )

    list_editable = ('username', 'is_active')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('role', 'is_active', 'is_superuser')
    list_per_page = 2

    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        ('Informations personnelles', {
            'fields': ('email', 'telephone', 'role'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'email',
                'telephone',
                'role',
            ),
        }),
    )

admin.site.register(Utilisateur, UserAdmin)
