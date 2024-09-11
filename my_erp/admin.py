from django.contrib import admin
from .models import NomencBook

# class MyExistingTableAdmin(admin.ModelAdmin):
#     list_display = ('idr_ref', 'other_field')  # Поля, которые будут отображаться в списке
#     search_fields = ('idr_ref', 'other_field')  # Поля, по которым будет производиться поиск
#     readonly_fields = ('idr_ref',)  # Поля, которые будут доступны только для чтения
# Register your models here.

class NomencBookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.write()

admin.site.register(NomencBook, NomencBookAdmin)