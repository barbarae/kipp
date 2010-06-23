"""
Convenience module for access of custom youtube application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.
"""
from django.conf import settings

# Autoplay
CMS_YOUTUBE_DEFAULT_AUTOPLAY = getattr(settings,
                                       'CMS_YOUTUBE_DEFAULT_AUTOPLAY', False)

# Width & Height
CMS_YOUTUBE_DEFAULT_WIDTH = getattr(settings, 'CMS_YOUTUBE_DEFAULT_WIDTH', 425)
CMS_YOUTUBE_DEFAULT_HEIGHT = getattr(settings, 'CMS_YOUTUBE_DEFAULT_HEIGHT', 
                                     344)

# Border
CMS_YOUTUBE_DEFAULT_BORDER = getattr(settings, 'CMS_YOUTUBE_DEFAULT_BORDER',
                                     False)

# Full Screen
CMS_YOUTUBE_DEFAULT_FULLSCREEN = getattr(settings,
                                         'CMS_YOUTUBE_DEFAULT_FULLSCREEN',
                                         True)

# Loop
CMS_YOUTUBE_DEFAULT_LOOP = getattr(settings, 'CMS_YOUTUBE_DEFAULT_LOOP', False)

# Display Related Videos
CMS_YOUTUBE_DEFAULT_RELATED = getattr(settings, 'CMS_YOUTUBE_DEFAULT_RELATED',
                                      False)

# High Quality
CMS_YOUTUBE_DEFAULT_HIGHQUALITY = getattr(settings,
                                          'CMS_YOUTUBE_DEFAULT_HIGHQUALITY',
                                          False)

