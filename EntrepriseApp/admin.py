from django.contrib import admin

from EntrepriseApp.models import Entreprise, Utilisateur

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
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


class UserAdmin(admin.ModelAdmin):
    list_display =(
        'user_id', 'username', 'email', 'role', 'is_active', 'is_superuser')
    list_editable = ('username','is_active', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('role', 'is_active', 'is_superuser')
    list_per_page = 2


admin.site.register(Utilisateur, UserAdmin)
