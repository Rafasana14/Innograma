import os
from .base import *

DEBUG = False

ADMINS = [
]
ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
CSRF_TRUSTED_ORIGINS = ["https://localhost:5000","http://localhost:5000"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'innograma_db',
        'PORT': 5432,
    }
}