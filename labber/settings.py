# Django settings for bicimap project. These work on my mac using manage.py runserver

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DOMAIN = 'http://localhost/' #We set up apache to host our media out of the MEDIA_ROOT
ROOT_DIR = '/Users/tombrown/Workspace/labber/'

ADMINS = (
     ('tombrown', 'tomfeelslucky@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ROOT_DIR + "db/db"             # Or path to database file if using sqlite3. Make sure that django can write to both the database file and its parent.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ROOT_DIR + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = DOMAIN + "media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8+@6v71p)c$d!sahl-zw#%_s9hi1i!@h&6r=884&zpkl6o$9cv'

#for sanity
APPEND_SLASH = True;

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    ROOT_DIR + "tmplts/",
    '/opt/local/lib/python2.5/site-packages/django/contrib/admin/templates/',
    '/opt/local/lib/python2.5/site-packages/django/contrib/comments/templates/'

)

TEMPLATE_CONTEXT_PROCESSORS = (
     'django.core.context_processors.auth',
     'django.core.context_processors.i18n',
     'django.core.context_processors.request',
     'django.core.context_processors.media',
     'zinnia.context_processors.media',
     'zinnia.context_processors.version', # Optional
  )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.admin', 
    'django.contrib.comments',
    'django.contrib.markup',
    'lablist'  
)
