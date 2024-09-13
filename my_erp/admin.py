from django.contrib import admin
from .models import NomencBook, ProductionType
from .forms import NomencBookAdminForm

class NomencBookAdmin(admin.ModelAdmin):
    form = NomencBookAdminForm
    list_display = ('name', 'field_code')
    def save_model(self, request, obj, form, change):
        obj.write()

class ProductionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'reproduction', 'display_name')

admin.site.register(ProductionType, ProductionTypeAdmin)
admin.site.register(NomencBook, NomencBookAdmin)