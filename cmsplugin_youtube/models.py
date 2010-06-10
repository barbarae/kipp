from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin

from cmsplugin_youtube import settings

class YouTube(CMSPlugin):
    video_id = models.CharField(_('video id'), max_length=60)

    autoplay = models.BooleanField(
        _('autoplay'),
        default=settings.CMS_YOUTUBE_DEFAULT_AUTOPLAY
    )

    width = models.IntegerField(_('width'),
            default=settings.CMS_YOUTUBE_DEFAULT_WIDTH)
    height = models.IntegerField(_('height'),
            default=settings.CMS_YOUTUBE_DEFAULT_HEIGHT)
    border = models.BooleanField(_('border'),
            default=settings.CMS_YOUTUBE_DEFAULT_BORDER)

    allow_fullscreen = models.BooleanField(
        _('allow fullscreen'),
        default=settings.CMS_YOUTUBE_DEFAULT_FULLSCREEN
    )

    loop = models.BooleanField(_('loop'),
            default=settings.CMS_YOUTUBE_DEFAULT_LOOP)

    display_related_videos = models.BooleanField(
        _('display related videos'),
        default=settings.CMS_YOUTUBE_DEFAULT_RELATED
    )

    high_quality = models.BooleanField(
        _('high quality'),
        default=settings.CMS_YOUTUBE_DEFAULT_HIGHQUALITY
    )

    def __unicode__(self):
        return u'%s' % (self.video_id,)
