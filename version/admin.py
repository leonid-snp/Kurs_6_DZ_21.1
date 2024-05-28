from django.contrib import admin
from version.models import Version


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'number', 'name', 'is_activ'
    )
    list_filter = ('product', 'is_activ')
    search_fields = ('product',)
