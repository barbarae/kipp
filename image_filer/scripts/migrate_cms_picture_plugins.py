from image_filer import models as image_filer_models
from django.utils.encoding import force_unicode
from image_filer.scripts.migrate_utils import get_image_instance_for_path

def migrate_picture_plugin_to_image_filer_publication(plugin_instance):
    if not plugin_instance.plugin_type == 'PicturePlugin':
        return
    from django.db import connection
    cursor = connection.cursor()
    
    instance, plugin = plugin_instance.get_plugin_instance()
    if not instance:
        return
    picture = instance.picture
    attr_map = {
            'cmsplugin_ptr_id'  : str(plugin_instance.id),
            'alt_text'          : u"'%s'" % picture.alt,
            'caption'           : u"'%s'" % picture.longdesc,
            'float'             : u"'%s'" % picture.float,
            'show_author'       : '0',
            'show_copyright'    : '0',
    }
    if picture.page_link_id in ['',None]:
        attr_map['page_link_id'] = 'NULL'
    else:
        attr_map['page_link_id'] = str(picture.page_link_id)
    try:
        image_filer_image = get_image_instance_for_path(force_unicode(picture.image))
        attr_map.update({
            'image_id'          : str(image_filer_image.id),
            'width'             : str(image_filer_image.width),
            'height'            : str(image_filer_image.height),
        })
    except Exception, e:
        print u"missing image! %s" % e
        return
    
    data = {'table_name': image_filer_models.ImagePublication._meta.db_table,
            'keys': ",".join('`%s`'%key for key in attr_map.keys()),
            'values': u",".join(attr_map.values()),
            }
    
    QUERY = '''INSERT INTO %(table_name)s (%(keys)s) VALUES (%(values)s);''' % data
    #print QUERY
    #cursor.execute(QUERY)
    QUERY_UPD = "UPDATE cms_cmsplugin SET plugin_type='ImagePlugin' WHERE id=%s;" % plugin_instance.id
    #print QUERY_UPD
    #cursor.execute(QUERY_UPD)
    QUERY_DEL = 'DELETE FROM cmsplugin_picture WHERE cmsplugin_ptr_id=%s;' % str(plugin_instance.id)
    #print QUERY_DEL
    #cursor.execute(QUERY_DEL)
    cursor.execute(QUERY+QUERY_UPD+QUERY_DEL)

def migrate_all():
    from cms.models import CMSPlugin
    for plugin in CMSPlugin.objects.filter(plugin_type='PicturePlugin'):
        migrate_picture_plugin_to_image_filer_publication(plugin)