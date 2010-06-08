
from south.db import db
from django.db import models
from image_filer.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ImagePublication'
        db.create_table('cmsplugin_filer', (
            ('cmsplugin_ptr', orm['image_filer.imagepublication:cmsplugin_ptr']),
            ('image', orm['image_filer.imagepublication:image']),
            ('alt_text', orm['image_filer.imagepublication:alt_text']),
            ('caption', orm['image_filer.imagepublication:caption']),
            ('width', orm['image_filer.imagepublication:width']),
            ('height', orm['image_filer.imagepublication:height']),
            ('show_author', orm['image_filer.imagepublication:show_author']),
            ('show_copyright', orm['image_filer.imagepublication:show_copyright']),
        ))
        db.send_create_signal('image_filer', ['ImagePublication'])
        
        # Adding model 'ClipboardItem'
        db.create_table('image_filer_clipboarditem', (
            ('id', orm['image_filer.clipboarditem:id']),
            ('file', orm['image_filer.clipboarditem:file']),
            ('clipboard', orm['image_filer.clipboarditem:clipboard']),
            ('is_checked', orm['image_filer.clipboarditem:is_checked']),
        ))
        db.send_create_signal('image_filer', ['ClipboardItem'])
        
        # Adding model 'Clipboard'
        db.create_table('image_filer_clipboard', (
            ('id', orm['image_filer.clipboard:id']),
            ('user', orm['image_filer.clipboard:user']),
        ))
        db.send_create_signal('image_filer', ['Clipboard'])
        
        # Deleting field 'Image.tree_id'
        db.delete_column('image_filer_image', 'tree_id')
        
        # Deleting field 'Image.lft'
        db.delete_column('image_filer_image', 'lft')
        
        # Deleting field 'Image.manipulation_profile'
        db.delete_column('image_filer_image', 'manipulation_profile_id')
        
        # Deleting field 'Image.level'
        db.delete_column('image_filer_image', 'level')
        
        # Deleting field 'Image.parent'
        db.delete_column('image_filer_image', 'parent_id')
        
        # Deleting field 'Image.rght'
        db.delete_column('image_filer_image', 'rght')
        
        # Deleting model 'imagemanipulationtemplate'
        db.delete_table('image_filer_imagemanipulationtemplate')
        
        # Deleting model 'bucket'
        db.delete_table('image_filer_bucket')
        
        # Deleting model 'bucketitem'
        db.delete_table('image_filer_bucketitem')
        
        # Deleting model 'imagemanipulationstep'
        db.delete_table('image_filer_imagemanipulationstep')
        
        # Deleting model 'imagemanipulationprofile'
        db.delete_table('image_filer_imagemanipulationprofile')
        
        # Deleting model 'imagepermission'
        db.delete_table('image_filer_imagepermission')
        
        # Changing field 'FolderPermission.can_read'
        # (to signature: django.db.models.fields.BooleanField(default=True, blank=True))
        db.alter_column('image_filer_folderpermission', 'can_read', orm['image_filer.folderpermission:can_read'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'ImagePublication'
        db.delete_table('cmsplugin_filer')
        
        # Deleting model 'ClipboardItem'
        db.delete_table('image_filer_clipboarditem')
        
        # Deleting model 'Clipboard'
        db.delete_table('image_filer_clipboard')
        
        # Adding field 'Image.tree_id'
        db.add_column('image_filer_image', 'tree_id', orm['image_filer.image:tree_id'])
        
        # Adding field 'Image.lft'
        db.add_column('image_filer_image', 'lft', orm['image_filer.image:lft'])
        
        # Adding field 'Image.manipulation_profile'
        db.add_column('image_filer_image', 'manipulation_profile', orm['image_filer.image:manipulation_profile'])
        
        # Adding field 'Image.level'
        db.add_column('image_filer_image', 'level', orm['image_filer.image:level'])
        
        # Adding field 'Image.parent'
        db.add_column('image_filer_image', 'parent', orm['image_filer.image:parent'])
        
        # Adding field 'Image.rght'
        db.add_column('image_filer_image', 'rght', orm['image_filer.image:rght'])
        
        # Adding model 'imagemanipulationtemplate'
        db.create_table('image_filer_imagemanipulationtemplate', (
            ('profile', orm['image_filer.image:profile']),
            ('description', orm['image_filer.image:description']),
            ('pre_cache', orm['image_filer.image:pre_cache']),
            ('identifier', orm['image_filer.image:identifier']),
            ('id', orm['image_filer.image:id']),
            ('name', orm['image_filer.image:name']),
        ))
        db.send_create_signal('image_filer', ['imagemanipulationtemplate'])
        
        # Adding model 'bucket'
        db.create_table('image_filer_bucket', (
            ('files', orm['image_filer.image:files']),
            ('id', orm['image_filer.image:id']),
            ('user', orm['image_filer.image:user']),
        ))
        db.send_create_signal('image_filer', ['bucket'])
        
        # Adding model 'bucketitem'
        db.create_table('image_filer_bucketitem', (
            ('is_checked', orm['image_filer.image:is_checked']),
            ('bucket', orm['image_filer.image:bucket']),
            ('id', orm['image_filer.image:id']),
            ('file', orm['image_filer.image:file']),
        ))
        db.send_create_signal('image_filer', ['bucketitem'])
        
        # Adding model 'imagemanipulationstep'
        db.create_table('image_filer_imagemanipulationstep', (
            ('description', orm['image_filer.image:description']),
            ('name', orm['image_filer.image:name']),
            ('order', orm['image_filer.image:order']),
            ('data', orm['image_filer.image:data']),
            ('id', orm['image_filer.image:id']),
            ('template', orm['image_filer.image:template']),
            ('filter_identifier', orm['image_filer.image:filter_identifier']),
        ))
        db.send_create_signal('image_filer', ['imagemanipulationstep'])
        
        # Adding model 'imagemanipulationprofile'
        db.create_table('image_filer_imagemanipulationprofile', (
            ('show_in_library', orm['image_filer.image:show_in_library']),
            ('description', orm['image_filer.image:description']),
            ('name', orm['image_filer.image:name']),
            ('id', orm['image_filer.image:id']),
        ))
        db.send_create_signal('image_filer', ['imagemanipulationprofile'])
        
        # Adding model 'imagepermission'
        db.create_table('image_filer_imagepermission', (
            ('can_add_children', orm['image_filer.image:can_add_children']),
            ('can_edit', orm['image_filer.image:can_edit']),
            ('group', orm['image_filer.image:group']),
            ('user', orm['image_filer.image:user']),
            ('can_read', orm['image_filer.image:can_read']),
            ('image', orm['image_filer.image:image']),
            ('type', orm['image_filer.image:type']),
            ('id', orm['image_filer.image:id']),
            ('everybody', orm['image_filer.image:everybody']),
        ))
        db.send_create_signal('image_filer', ['imagepermission'])
        
        # Changing field 'FolderPermission.can_read'
        # (to signature: django.db.models.fields.BooleanField(default=False, blank=True))
        db.alter_column('image_filer_folderpermission', 'can_read', orm['image_filer.folderpermission:can_read'])
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'menu_login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'image_filer.clipboard': {
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['image_filer.Image']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clipboards'", 'to': "orm['auth.User']"})
        },
        'image_filer.clipboarditem': {
            'clipboard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Clipboard']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'image_filer.folder': {
            'Meta': {'unique_together': "(('parent', 'name'),)"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'image_filer.folderpermission': {
            'can_add_children': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_edit': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_read': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'everybody': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Folder']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'image_filer.image': {
            '_height_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width_field': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_use_for_print': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_private_use': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_research': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_teaching': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'can_use_for_web': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_of_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'image_files'", 'null': 'True', 'to': "orm['image_filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_images'", 'null': 'True', 'to': "orm['auth.User']"}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'usage_restriction_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'image_filer.imagepublication': {
            'Meta': {'db_table': "'cmsplugin_filer'"},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['image_filer.Image']"}),
            'show_author': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'show_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['image_filer']
