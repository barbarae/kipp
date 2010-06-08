from django import forms
from django.conf import settings
from filer.settings import FILER_MEDIA_PREFIX

ADMIN_MEDIA_PREFIX = settings.ADMIN_MEDIA_PREFIX

class Browser(forms.Form):
    class Media:
        #css = {
        #    'all': ('/media/javascript/jquery/external/jquery-autocomplete/jquery.autocomplete-django.css',)
        #}
        js = (
            '%sjs/admin/RelatedObjectLookups.js' % ADMIN_MEDIA_PREFIX,
            '%sjs/popup_handling.js' % FILER_MEDIA_PREFIX,
            '%sjs/jquery-1.3.2.min.js' % FILER_MEDIA_PREFIX,
            '%sjs/jquery-ui-1.7.2.custom.min.js' % FILER_MEDIA_PREFIX,
            '%sjs/jquery.cookie.js' % FILER_MEDIA_PREFIX,
            '%sjs/swfupload.js' % FILER_MEDIA_PREFIX,
            '%sjs/swfupload.queue.js' % FILER_MEDIA_PREFIX,
        )