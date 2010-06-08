from pprint import pprint
from filer import models
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import simplejson
from filer.settings import FILER_STATICMEDIA_PREFIX


def get_folder_for_rel(ref_id, ref_objtype, ref_type):
    if ref_objtype == 'folder':
        reference_obj = models.Folder.objects.get(id=ref_id)
        if ref_type in ['before','after']:
            # the destination obj is on the same level as reference_obj
            if reference_obj.parent:
                destination_obj = reference_obj.parent
            else:
                destination_obj = None
        elif ref_type == 'inside':
            destination_obj = reference_obj
        else:
            print 'error!'
            return None
    elif ref_objtype == 'file':
        reference_obj = models.File.objects.get(id=ref_id)
        if ref_type in ['before','after']:
            destination_obj = reference_obj.folder
        else: # inside or anything else
            # this is illegal. a file cant have subitems!
            print 'error!'
            return None
    else:
        print 'unknown obj type %s!' % ref_objtype
        return None
    return destination_obj

def build_file_dict(file):
    file = file.subtype()
    r = {}
    #{ title : "Node title", icon : "path_to/icon.pic", attributes : {"key" : "value" } }
    #pprint (file.icons)
    r['data'] = { 'title' : unicode(file.label), 'icon' : file.icons.get('16', '')}
    r['attributes'] = {'id': file.id, "rel":"file" }
    return r

def build_folder_dict(folder, id_override=None, include_files=True, max_depth=None, hint_children=True, depth=0):
    r = {}
    r['data'] = unicode(folder)
    if id_override is None:
        r['attributes'] = {'id': folder.id, "rel":"folder" }
    else:
        r['attributes'] = {'id': id_override, "rel":"folder" }
    children = folder.children.all()
    files = folder.files
    print "handling '%s' children: %s depth: %s max_depth: %s" % (folder, len(children), depth, max_depth)
    show_children = max_depth is None or max_depth>depth
    r['children'] = []
    if show_children:
        if len(children):
            print u"%s creating children for '%s' because %s is larger than %s" % (" "*depth, folder, max_depth, depth )
            for child in children:
                print u"forloop %s" % child
                r['children'].append(build_folder_dict(child, include_files=include_files, max_depth=max_depth, hint_children=hint_children, depth=depth+1))
        if include_files:
            if len(files):
                for file in files:
                    r['children'].append(build_file_dict(file))
    elif len(children) or len(files):
        print u"%s marking '%s' as closed because it has %s children" % (" "*depth, folder, len(children) )
        if hint_children:
            r['state'] = 'closed'
    if not len(r['children']):
        del r['children']
    return r

def build_category_node(title,name,children):
    return {
        "data": {
            "title":title,
            "attributes":{"class":"noicon"}
        },
        "state": "open", 
        "attributes":{
            "id":name,
            "class":"noicon",
            "rel":"category",
        }, 
        "children":children,
    }

def initial_folder_view(user):
    root_folders = []
    folders = models.Folder.objects.filter(parent=None).order_by('name')
    for folder in folders:
        root_folders.append(build_folder_dict(folder, include_files=False, max_depth=0, hint_children=False))
    root_folders_category = build_category_node("FOLDERS", "rootFoldersCategory", root_folders)
    
    special_folders = [
        build_folder_dict(models.UnfiledImages(), include_files=False, hint_children=False, max_depth=0 ),
        build_folder_dict(models.ImagesWithMissingData(), include_files=False, hint_children=False, max_depth=0)
    ]
    special_folders_category = build_category_node("SPECIAL FOLDERS", "specialCategory", special_folders)
    favorite_folders = []
    for folder in models.Folder.objects.filter(favoritefolder__user=user).order_by('name'):
        favorite_folders.append(build_folder_dict(folder, include_files=False, max_depth=0, hint_children=False))
    favorites_category = build_category_node("favoritesCategory", "favoritesCategory", favorite_folders)
    categories_data = [root_folders_category, special_folders_category, favorites_category]
    
    # TODO: catch if there are no root folders!
    folders_data = []
    for child in folders[0].children.order_by('name'):
        folders_data.append(build_folder_dict(child))
    
    try:
        selected_category_id = folders[0].id
    except:
        selected_category_id = 'unfiled_folder'
    
    return {'folders_data': folders_data,
            'categories_data': categories_data,
            'selected_category_id': selected_category_id}



class Browser(object):
    def json_folder(self, request, extra_context=None):
        folder_id = request.REQUEST.get('id', None)
        print "Browser.json_folder: %s" % folder_id
        structured_data = self.get_folder(folder_id)
        return HttpResponse(simplejson.dumps(structured_data),mimetype='application/json')
    def get_folder(self, folder_id):
        structured_data = []
        if folder_id is None:
            return HttpResponse(simplejson.dumps([]),mimetype='application/json')
        elif folder_id == models.UnfiledImages.id:
            print 'unifiled'
            data = build_folder_dict(models.UnfiledImages())
        elif folder_id == models.ImagesWithMissingData.id:
            print 'missing'
            data = build_folder_dict(models.ImagesWithMissingData())
        else:
            print "normal id"
            folder = models.Folder.objects.get(pk=folder_id)
            data = build_folder_dict(folder, max_depth=1)
        if 'children' in data:
            structured_data = data['children']
        else:
            structured_data = []
        pprint(structured_data)
        return structured_data
    
    def json_move(self, request, extra_context=None):
        #TODO: Permission checking!!!!!
        try:
            src_objtype = request.POST.get('src_objtype', None)
            src_id = request.POST.get('src_id', None)
            ref_objtype = request.POST.get('ref_objtype', None) 
            ref_id = request.POST.get('ref_id', None) 
            ref_type = request.POST.get('ref_type', None) 
            print "src_type: %s src_id: %s ref_objtype: %s ref_id: %s ref_type: %s" % (src_objtype, src_id, ref_objtype, ref_id, ref_type)
            if src_objtype in ['folder','file','category'] and src_id and ref_objtype and ref_id and ref_type:
                if ref_objtype == 'folder':
                    reference_obj = models.Folder.objects.get(id=ref_id)
                    if ref_type in ['before','after']:
                        # the destination obj is on the same level as reference_obj
                        if reference_obj.parent:
                            destination_obj = reference_obj.parent
                        else:
                            destination_obj = None
                    else: #'inside'
                        destination_obj = reference_obj
                elif ref_objtype == 'file':
                    reference_obj = models.File.objects.get(id=ref_id)
                    if ref_type in ['before','after']:
                        destination_obj = reference_obj.folder
                    else:
                        # this is illegal. a file cant have subitems!
                        destination_obj = reference_obj.folder
                
                print u"got destination folder '%s'" % destination_obj
                
                if src_objtype == 'folder':
                    src_folder = models.Folder.objects.get(id=src_id)
                    src_folder.parent = destination_obj
                    src_folder.save()
                    print "moved folder"
                elif src_objtype == 'file':
                    src_file = models.File.objects.get(id=src_id)
                    src_file.folder = destination_obj
                    src_file.save()
                    print "moved file"
                elif src_objtype is 'category' and src_id is 'favorites':
                    print "category type"
                else:
                    print "unknown type"
            else:
                print "somethign is wrong"
        except Exception, e:
            print e
            HttpResponse(simplejson.dumps({'result':'failed'}),mimetype='application/json')
        return HttpResponse(simplejson.dumps({'result':'ok'}),mimetype='application/json')
    def json_rename(self, request, extra_context=None):
        # TODO: check for permissions!
        obj_id = request.POST.get('obj_id', None)
        obj_type = request.POST.get('obj_type', None)
        obj_new_name = request.POST.get('obj_new_name', None)
        print "json_rename id: %s type: %s new_name: %s" % (obj_id, obj_type, obj_new_name)
        if obj_id and obj_type and obj_new_name:
            if obj_type == 'folder':
                obj = models.Folder.objects.get(id=obj_id)
            elif obj_type == 'file':
                obj = models.File.objects.get(id=obj_id)
            else:
                print "unknown type '%s'" % obj_type
                return HttpResponse(simplejson.dumps({'result':'failed'}),mimetype='application/json')
            obj.name = obj_new_name
            obj.save()
        return HttpResponse(simplejson.dumps({'result':'ok'}),mimetype='application/json')
    
    def json_create(self, request, extra_context=None):
        # TODO: check for permissions!
        node_name = request.POST.get('node_name', None)
        node_type = request.POST.get('node_type', None)
        ref_node_id = request.POST.get('ref_node_id', None)
        ref_node_type = request.POST.get('ref_node_type', None)
        ref_node_rel = request.POST.get('ref_node_rel', None)
        print "json_create new '%s' named '%s' at '%s' of '%s (%s)'" % (node_type, node_name, ref_node_rel, ref_node_id, ref_node_type)
        if node_type == 'folder':
            new_folder = models.Folder(name=node_name)
            parent_folder = get_folder_for_rel(ref_node_id, ref_node_type, ref_node_rel)
            new_folder.parent = parent_folder
            new_folder.save()
        return HttpResponse(simplejson.dumps({'result':'ok'}),mimetype='application/json')