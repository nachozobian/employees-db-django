from .base import *
# SECURITY WARNING: don't run with debug turned on in productioS!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'nachozobian',
        'PASSWORD': 'Tamadaba21',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')