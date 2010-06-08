from django.db import models
from django.contrib.auth import models as auth_models

from filer.models.foldermodels import Folder
from filer.models import mixins

class FavoriteFolder(models.Model, mixins.IconsMixin):
    _icon = 'plainfolder'
    file_type = 'FavoriteFolder'
    user = models.ForeignKey(auth_models.User)
    folder = models.ForeignKey(Folder)
    
    @property
    def name(self):
        return self.folder.name
    
    def __unicode__(self):
        return u"%s: %s" % (self.user, self.folder)
    class Meta:
        app_label = 'filer'
        unique_together = (('user','folder',),)