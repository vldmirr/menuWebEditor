from django import template
from django.core.exceptions import ImproperlyConfigured
from menu_app.utils import get_menu_data

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Template tag to draw menu by name"""
    request = context.get('request')
    
    if not request:
        raise ImproperlyConfigured(
            "The 'request' context processor is required. "
            "Add 'django.template.context_processors.request' to your TEMPLATES setting."
        )
    
    menu_tree = get_menu_data(menu_name, request)
    
    return {
        'menu_tree': menu_tree,
        'menu_name': menu_name,
    }