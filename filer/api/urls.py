from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from piston.doc import documentation_view
from filer.api.handlers import FolderHandler, ItemGroupHandler, FileHandler

item_group_handler = Resource(ItemGroupHandler)
folder_handler = Resource(FolderHandler)
file_handler = Resource(FileHandler)


urlpatterns = patterns('',
    url(r'^item_group/$', item_group_handler), # return all categories
    
    url(r'^folder/(?P<id>[^/]+)/$', folder_handler),
    #url(r'^folder/children/$', folder_handler, {'filter':'children'}), # all root folders
    url(r'^folder/(?P<id>[^/]+)/children/$', folder_handler, {'filter_mode':'children'}), # all children of folder id. id can be 'root'
    url(r'^folder/$', folder_handler),
    
    url(r'^file/(?P<id>[^/]+)/$', file_handler),
    
    
    
)