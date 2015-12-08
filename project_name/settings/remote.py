from .base import *
from .cred import ODB, ODB_U, ODB_PW

ALLOWED_HOSTS = ['.example.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ODB,
        'USER': ODB_U,
        'PASSWORD': ODB_PW,
        'HOST': 'localhost',
        'PORT': '',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME':ODB,
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': ODB,
#         'USER': ODB_U,
#         'PASSWORD':ODB_PW,
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
