from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    search_fields = ('name', 'menu_name')
    fields = ('name', 'menu_name', 'named_url', 'explicit_url', 'parent', 'order')
    ordering = ('menu_name', 'order', 'name')


admin.site.register(MenuItem, MenuItemAdmin)