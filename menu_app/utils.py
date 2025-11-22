from django.urls import resolve, Resolver404
from .models import MenuItem


def get_current_path(request):
    """Get current path from request"""
    return request.path


def is_active_url(item_url, current_path):
    """Check if menu item URL matches current path"""
    if not item_url or item_url == '#':
        return False
    
    # Normalize URLs for comparison
    item_url = item_url.rstrip('/')
    current_path = current_path.rstrip('/')
    
    return item_url == current_path


def build_menu_tree(menu_items, current_path, parent=None):
    """Build hierarchical menu structure with active states"""
    tree = []
    
    for item in menu_items:
        if item.parent == parent:
            children = build_menu_tree(menu_items, current_path, item)
            
            # Check if this item or any of its children is active
            item_url = item.get_url()
            is_active = is_active_url(item_url, current_path)
            has_active_child = any(child['is_active'] or child['has_active_child'] for child in children)
            
            tree.append({
                'item': item,
                'children': children,
                'is_active': is_active,
                'has_active_child': has_active_child,
                'is_expanded': is_active or has_active_child,
            })
    
    return tree


def get_menu_data(menu_name, request):
    """Get menu data with single database query"""
    # Get all menu items for this menu in one query
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name
    ).select_related('parent').prefetch_related('children').order_by('order', 'name')
    
    current_path = get_current_path(request)
    
    # Build menu tree
    menu_tree = build_menu_tree(menu_items, current_path)
    
    return menu_tree