import os

gettext = lambda s: s
# Django settings for kipp project.

PROJECT_ROOT = os.path.dirname(__file__)

ADMINS = (
    ('Matthew Irish', 'matthew.irish@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

URL_FILEBROWSER_MEDIA = '/media/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = '/media/filebrowser/'
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_DEBUG = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '79m=eg)ookdws%fz%6*&@)n@n-j1)g(^07@wrqltq%6j)0boi&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        "django.core.context_processors.i18n",
        "django.core.context_processors.request",
        "django.core.context_processors.media",
        'image_filer.context_processors.media',
        "cms.context_processors.media",
        'zinnia.context_processors.media',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware', 
    'django.middleware.locale.LocaleMiddleware',
)

LANGUAGE_CODE = 'en'

LANGUAGES = (
        ('en', gettext('English')),
)

ROOT_URLCONF = 'kipp.urls'

CMS_TEMPLATES = (
        ('page.html', gettext('default')),
        ('base.html', gettext('Home page')),
        ('2col.html', gettext('2 Column')),
        ('3col.html', gettext('3 Column')),
        ('extra.html', gettext('Some extra fancy template')),
)
ZINNIA_MEDIA_URL = '/media/zinnia/'
CMS_SHOW_END_DATE = True
CMS_SHOW_START_DATE = True
CMS_PERMISSION = True
CMS_MODERATOR = False
CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS" : False,
}
INTERNAL_IPS = ('127.0.0.1',)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'debug_toolbar',
    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'publisher',
    'menus',
    'typogrify',
    'tagging',
    'zinnia',
    'zinnia.plugins',
    'sorl.thumbnail',
    'image_filer',
    'reversion',
    'cmsplugin_faq',
    'cmsplugin_youtube',
    'contact',
)
