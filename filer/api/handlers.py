from piston.handler import BaseHandler
from piston.utils import rc
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from filer import models
from mptt.exceptions import InvalidMove

from pprint import pprint

import sys, traceback


class NodeHandler(BaseHandler):
    allowed_methods = ('GET',)
    fields = ('id','name','node_type','file_type','icon', 'icons')
    
    
    @classmethod
    def name(cls, obj):
        if hasattr(obj, 'label'):
            return obj.label
        elif hasattr(obj, 'name'):
            return obj.name
        else:
            return unicode(obj)
    
    @classmethod
    def node_type(cls, obj):
        # node_type is either folder or file
        return ("%s" % obj.file_type).lower()
    @classmethod
    def file_type(cls, obj):
        # the exact file type (needed for filtering)
        if obj.file_type.lower() == 'file':
            return ("%s" % obj.subtype().file_type).lower()
        else:
            return 'folder'
    
    @classmethod
    def icon(cls, obj):
        return obj.icons['16']
    
    def update(self, request, *args, **kwargs):
        if not self.has_model():
            return rc.NOT_IMPLEMENTED
        pkfield = self.model._meta.pk.name

        if pkfield not in kwargs:
            # No pk was specified
            return rc.BAD_REQUEST

        try:
            inst = self.queryset(request).get(pk=kwargs.get(pkfield))
        except ObjectDoesNotExist:
            return rc.NOT_FOUND
        except MultipleObjectsReturned: # should never happen, since we're using a PK
            return rc.BAD_REQUEST
        attrs = self.flatten_dict(request.data)
            
        for k,v in attrs.iteritems():
            if k == 'parent':
                if v == 'favoritesCategory':
                    # don't actually move the folder... just add a favorite
                    new_favorite = models.FavoriteFolder(folder=inst, user=request.user)
                    new_favorite.save()
                else:
                    try:
                        parent_id = int(v)
                        parent = models.Folder.objects.get(pk=parent_id)
                    except:
                        parent = None
                    inst.parent = parent
            elif k == 'folder':
                try:
                    folder_id = int(v)
                    folder = models.Folder.objects.get(pk=folder_id)
                except:
                    folder = None
                inst.folder = folder  
            #elif k == 'name':
            #    inst.name = self.find_free_folder_name(inst.parent, v)
            else:
                setattr( inst, k, v )
        try:
            inst.save()
        except InvalidMove, e:
            # mptt error e.g when there is a circular tree 
            #traceback.print_exc(file=sys.stdout)
            return rc.BAD_REQUEST
        return rc.ALL_OK

class FolderHandler(NodeHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    model = models.Folder
    fields = list(NodeHandler.fields) + ['has_children', 'children_count','file_count','item_count',]
    
    def read(self, request, *args, **kwargs):
        if not self.has_model(): # we know this will never happen ;-)
            return rc.NOT_IMPLEMENTED
        user = request.user
        pkfield = self.model._meta.pk.name
        pk = kwargs.get(pkfield)
        filter_mode = kwargs.get('filter_mode', None)
        if filter_mode=='children':
            if pk == 'root':
                qs = self.queryset(request).filter(parent__isnull=True)
                return qs
            elif pk == 'unfiled_files':
                return models.UnfiledImages().files
            elif pk == 'images_with_missing_data':
                return models.ImagesWithMissingData().files
            elif pk:
                qs_folders = self.queryset(request).filter(parent=pk)
                qs_files = models.File.objects.filter(folder=pk)
                return list(qs_folders) + list(qs_files)  
        if pkfield in kwargs:
            try:
                if pk == 'root':
                    return ItemGroupHandler.item_groups(user)['rootFoldersCategory']
                elif pk == 'unfiled_files':
                    return models.UnfiledImages().as_deep_dict()
                elif pk == 'images_with_missing_data':
                    return models.ImagesWithMissingData().as_deep_dict()
                else:
                    return self.queryset(request).get(pk=kwargs.get(pkfield))
            except ObjectDoesNotExist:
                return rc.NOT_FOUND
            except MultipleObjectsReturned: # should never happen, since we're using a PK
                return rc.BAD_REQUEST
        else:
            return self.queryset(request).filter(*args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if not self.has_model():
            return rc.NOT_IMPLEMENTED
        
        attrs = self.flatten_dict(request.data)
            
        if 'parent' in attrs.keys():
            parent = models.Folder.objects.get(pk=attrs['parent'])
        else:
            parent = None
        
        if 'name' in attrs.keys():
            basename = attrs['name']
        else:
            basename = "New Folder" 
        name = self.find_free_folder_name(parent, basename)
        inst = self.model(name=name,parent=parent)
        inst.save()
        return inst
        
    def find_free_folder_name(self, parent, basename, number=0):
        if number:
            name = u"%s %s" % (basename, number)
        else:
            name = basename 
        if not self.model.objects.filter(name=name, parent=parent).count()>0:
            # name is free
            return name
        else:
            # this name is already taken. try again
            return self.find_free_folder_name(parent=parent, basename=basename, number=number+1)
class FileHandler(NodeHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    model = models.File
    
    @classmethod
    def icon(cls, obj):
        return obj.subtype().icons['16']
        


class ItemGroupHandler(NodeHandler):
    allowed_methods = ('GET',)
    fields = list(NodeHandler.fields) + ['children',]
    
    @classmethod
    def item_groups(cls, user):
        ITEM_GROUPS = {
            'rootFoldersCategory':{
                'id': 'rootFoldersCategory',
                'node_type': 'category',
                'name': 'FOLDERS',
                'children': models.Folder.objects.filter(parent__isnull=True),
            },
            'specialCategory':{
                'id': 'specialCategory',
                'node_type': 'category',
                'name':'SPECIAL',
                'children': [models.UnfiledImages().as_dict(), models.ImagesWithMissingData().as_dict()],
            },
            'favoritesCategory':{
                'id': 'favoritesCategory',
                'node_type': 'category',
                'name': 'FAVORITES',
                'children': models.Folder.objects.filter(favoritefolder__user=user),
             },
        }
        return ITEM_GROUPS
    
    def read(self, request, *args, **kwargs):
        pk = kwargs.get('id', None)
        if pk:
            if pk in self.item_groups(user=request.user).keys():
                return self.item_groups(user=request.user)[pk]
            return rc.NOT_FOUND
        else:
            return self.item_groups(user=request.user).values()