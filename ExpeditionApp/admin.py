from django.contrib import admin

from OffreApp.models import Offre
from ExpeditionApp.models import Expedition
from django.utils import timezone

class EnRetardFilter(admin.SimpleListFilter):
    title = 'en retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return [
            ('oui', 'Oui'),
            ('non', 'Non'),
        ]

    def queryset(self, request, queryset):
        aujourd_hui = timezone.localdate()

        if self.value() == 'oui':
            return queryset.filter(
                status='p',
                date_souhaitee__lt=aujourd_hui,
            )

        if self.value() == 'non':
            return queryset.exclude(
                status='p',
                date_souhaitee__lt=aujourd_hui,
            )

        return queryset
class OffreInline(admin.StackedInline):
    model = Offre
    extra = 0
    fk_name = 'expedition'

    fields = (
        'transporteur',
        'vehicule',
        'prix',
        'delai_jours',
        'statut',
    )
    readonly_fields = fields

    show_change_link = True
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False
@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('references', 'ville_depart', 'ville_arrivee', 'date_souhaitee', 'status', 'entreprise')
    search_fields = ('references', 'ville_depart', 'ville_arrivee')
    list_filter = ('status', 'date_souhaitee',EnRetardFilter)
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
    inlines = [OffreInline]