from menus.menu_pool import menu_pool
from menus.templatetags.menu_tags import cut_levels, show_menu, cut_after
from django import template

register = template.Library()

@register.inclusion_tag("parent_page_title.html",takes_context=True)  
def parent_page_title(context):
    """
    Returns the name of the parent page of the current node
    """
    try:
        # If there's an exception (500), default context_processors may not be called.
        request = context['request']
    except KeyError:
        return {'template': 'menu/empty.html'}
    nodes = menu_pool.get_nodes(request)
    parent_node = None
    for node in nodes:
        if (node.level == 1) or (node.get_attribute("reverse_id")=="get-involved"): 
            if (node.ancestor) or (node.selected):
                parent_node = node
                
    context.update({"parent_page":parent_node})
    return context



@register.inclusion_tag('cms/dummy.html', takes_context=True)                                
def kipp_sub_menu(context, template="menu/sub_menu.html"):
    try:
        # If there's an exception (500), default context_processors may not be called.
        request = context['request']
    except KeyError:
        return {'template': 'menu/empty.html'}
    nodes = menu_pool.get_nodes(request)
    parent_node = None
    children = []    
    for node in nodes:
        if (node.level == 1) or (node.get_attribute("reverse_id")=="get-involved"): 
            if (node.ancestor) or (node.selected):
                parent_node = node
            if parent_node is None:
                pass
            else:
                children = parent_node.children
    context.update({'children':children,
                    'template':template,
                    'from_level':0,
                    'to_level':0,
                    'extra_inactive':0,
                    'extra_active':0
                    })
    return context 

