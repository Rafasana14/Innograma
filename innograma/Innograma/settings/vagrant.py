import os
from .base import *

DEBUG = True

ADMINS = [
]
ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'static/media'
CSRF_TRUSTED_ORIGINS = ["https://localhost:8000","http://localhost:8000"]

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
