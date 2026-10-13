from django.contrib import admin

from EntrepriseApp.models import Entreprise, Utilisateur

class UserAdmin(admin.ModelAdmin):
    list_display =(
        'user_id', 'username', 'email', 'role', 'is_active', 'is_superuser')
    list_editable = ('username','is_active', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    list_filter = ('role', 'is_active', 'is_superuser')
    list_per_page = 2
# Register your models here.
admin.site.register(Entreprise)
admin.site.register(Utilisateur, UserAdmin)