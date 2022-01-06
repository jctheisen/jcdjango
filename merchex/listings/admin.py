from django.contrib import admin
from listings.models import Groupe, Fetiche

class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_crea', 'genre', 'biographie')


class FeticheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_crea', 'type_support', 'groupe')


admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Fetiche, FeticheAdmin)
