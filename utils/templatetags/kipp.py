from menus.menu_pool import menu_pool
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
        if (node.level == 0): 
            if (node.ancestor) or (node.selected):
                parent_node = node
                
    context.update({"parent_page":parent_node})
    return context

