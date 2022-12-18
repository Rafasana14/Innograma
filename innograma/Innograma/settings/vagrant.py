import os
from .base import *

DEBUG = True

ADMINS = [
]
ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
CSRF_TRUSTED_ORIGINS = ["https://localhost:5000","http://localhost:5000"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'innograma',
        'USER': 'innograma',
        'PASSWORD': 'innograma',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
