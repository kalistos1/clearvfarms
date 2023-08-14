from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# routers for tenancy
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'farm',
        'USER': 'postgres',
        'PASSWORD': 'kal15t05',
        'HOST': '127.0.0.1',  # or the IP address of your PostgreSQL server
        'PORT': '5432',       # PostgreSQL's default port is 5432
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


STATICFILES_DIRS = [
    BASE_DIR/ "static", "./static/",
]
