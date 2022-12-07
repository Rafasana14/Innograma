from .base import *

DEBUG = False

ADMINS = [
    # A RELLENAR
    # ('Antonio M', 'email@mydomain.com'),
]
ALLOWED_HOSTS = ['*']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "Innograma",
        "USER": "postgres",
        "PASSWORD": "d@m@nt1v@m1gr@f",
        "HOST": "localhost",
        "PORT": "5432",
    }
}