from .base import *
from .cred import ODB, ODB_U, ODB_PW

LOCAL_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
)


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}

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
