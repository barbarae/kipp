from menus.menu_pool import menu_pool
from menus.templatetags.menu_tags import cut_levels
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
def kipp_main_menu(context, from_level=0, to_level=100, extra_inactive=0, extra_active=100, template="menu/menu.html", namespace=None, root_id="main", next_page=None,):
    try:
        # If there's an exception (500), default context_processors may not be called.
        request = context['request']
    except KeyError:
        return {'template': 'menu/empty.html'}
    
    if next_page:
        children = next_page.children
    else: 
        #new menu... get all the data so we can save a lot of queries
        nodes = menu_pool.get_nodes(request, namespace, root_id)
        for n in nodes:
            if n.get_attribute("reverse_id") == "main":
                if root_id: # find the root id and cut the nodes
                    id_nodes = menu_pool.get_nodes_by_attribute(nodes, "reverse_id", root_id)
                    if id_nodes:
                        node = id_nodes[0]
                        new_nodes = node.children
                        for n in new_nodes:
                            n.parent = None
                        from_level += node.level + 1
                        to_level += node.level + 1
                    else:
                        new_nodes = []
                    nodes = new_nodes
                children = cut_levels(nodes, from_level, to_level, extra_inactive, extra_active)
                children = menu_pool.apply_modifiers(children, request, namespace, root_id, post_cut=True)
    
    try:
        context.update({'children':children,
                        'template':template,
                        'from_level':from_level,
                        'to_level':to_level,
                        'extra_inactive':extra_inactive,
                        'extra_active':extra_active,
                        'namespace':namespace})
    except:
        context = {"template":template}
    return context




