from django.utils.translation import ugettext_lazy as _
from filer.models.filemodels import File
from filer.models.foldermodels import Folder
from filer.models import mixins
from django.core import urlresolvers

class DummyFolder(mixins.IconsMixin):
    name = "Dummy Folder"
    is_root = True
    is_smart_folder = True
    can_have_subfolders = False
    parent = None
    _icon = "plainfolder"
    id="none"
    file_type = 'dummy'
    @property
    def virtual_folders(self):
        return []
    @property
    def children(self):
        return Folder.objects.filter(id__in=[0]) # empty queryset
    @property
    def files(self):
        return File.objects.filter(id__in=[0]) # empty queryset
    @property
    def items(self):
        return []
    parent_url = None
    @property
    def image_files(self):
        return self.files
    def __unicode__(self):
        return unicode(self.name)
    def as_dict(self):
        return {
                'id': u"%s" % self.id,
                'node_type': u"%s" % self.file_type,
                'name': u"%s" % self.name,
                #'children': self.files
                }


class UnfiledImages(DummyFolder):
    name = _("unfiled files")
    is_root = True
    _icon = "unfiled_folder"
    id="unfiled_files"
    file_type = 'Folder'
    def _files(self):
        return File.objects.filter(folder__isnull=True)
    files = property(_files)
    @property
    def items(self):
        return self.files
    def get_admin_directory_listing_url_path(self):
        return urlresolvers.reverse('admin:filer-directory_listing-unfiled_images')
    def as_deep_dict(self):
        d = self.as_dict()
        d['children'] = self.files
        return d
    
    
class ImagesWithMissingData(DummyFolder):
    name = _("files with missing metadata")
    is_root = True
    _icon = "incomplete_metadata_folder"
    id="images_with_missing_data"
    @property
    def files(self):
        return File.objects.filter(has_all_mandatory_data=False)
    @property
    def items(self):
        return self.files
    def get_admin_directory_listing_url_path(self):
        return urlresolvers.reverse('admin:filer-directory_listing-images_with_missing_data')
    def as_deep_dict(self):
        d = self.as_dict()
        d['children'] = self.files
        return d
    
class FolderRoot(DummyFolder):
    name = 'Root'
    is_root = True
    is_smart_folder = False
    can_have_subfolders = True
    id="root"
    @property
    def virtual_folders(self):
        return [UnfiledImages(), ]# ImagesWithMissingData()]
    @property
    def children(self):
        return Folder.objects.filter(parent__isnull=True) 
    parent_url = None
    def get_admin_directory_listing_url_path(self):
        return urlresolvers.reverse('admin:filer-directory_listing-root')