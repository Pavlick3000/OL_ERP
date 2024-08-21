from django.contrib import admin
from .models import TableOl

class TableOlAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age']
    exclude = ['id']

admin.site.register(TableOl, TableOlAdmin)