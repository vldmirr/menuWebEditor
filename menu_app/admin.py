# menu_app/admin.py
from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    fields = ('title', 'url', 'named_url', 'parent')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MenuItemInline]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'url', 'named_url')
    list_filter = ('menu',)
