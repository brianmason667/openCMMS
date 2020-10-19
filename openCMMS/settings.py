"""
Django settings for openCMMS project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
from datetime import timedelta

import ldap
from django_auth_ldap.config import LDAPSearch

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k&-js5nc7p%#$pk_bj+3fqd0($w5!6^#dy+a+b&p6($3r$a-%k'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('ENVIRONMENT') == 'PROD':
    DEBUG = False
else:
    DEBUG = True

################################################################
######################### GLOBAL CONF ##########################
################################################################

ALLOWED_HOSTS = [
    'application.lxc.pic.brasserie-du-slalom.fr',
    '127.0.0.1',
    'localhost',
    'dev.lxc.pic.brasserie-du-slalom.fr',
    'https://dev.lxc.pic.brasserie-du-slalom.fr/api/admin/login/?next=/api/admin/',
    'https://dev.lxc.pic.brasserie-du-slalom.fr/api/admin/',
    'https://dev.lxc.pic.brasserie-du-slalom.fr',
]

if os.getenv('ENVIRONMENT') == 'DEV':
    BASE_URL = 'https://dev.lxc.pic.brasserie-du-slalom.fr/'
elif os.getenv('ENVIRONMENT') == 'PROD':
    BASE_URL = 'https://application.lxc.pic.brasserie-du-slalom.fr/'

BASE_URL = 'http://localhost:4200/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.staticfiles', 'rest_framework', 'rest_framework_swagger', 'drf_yasg',
    'usersmanagement.apps.UsersmanagementConfig', 'maintenancemanagement.apps.MaintenancemanagementConfig',
    'utils.apps.UtilsConfig', 'django_inlinecss'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'openCMMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'utils/templates/')],
        'APP_DIRS': True,
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
            },
    },
]

WSGI_APPLICATION = 'openCMMS.wsgi.application'

AUTH_USER_MODEL = 'usersmanagement.UserProfile'

################################################################
########################## DATABASES ###########################
################################################################

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django',
            'USER': 'django',
            'PASSWORD': 'django',
            'HOST': 'localhost',
            'PORT': '',
        }
}

if os.getenv('ENVIRONMENT') == 'DEV':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '192.168.101.11',
        'PORT': '',
    }

if 'test' in sys.argv or 'pytest' in sys.argv[0] or os.getenv('ENVIRONMENT') == 'LOCAL':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '',
    }

if os.getenv('ENVIRONMENT') == 'PROD':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '192.168.101.10',
        'PORT': '',
    }

################################################################
############################ OTHERS ############################
################################################################

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS':
        'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication'
        ),
}

SWAGGER_SETTINGS = {'LOGIN_URL': "/api/admin/login"}

################################################################
############################ STATIC ############################
################################################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "utils/templates/"),
)

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')

################################################################
############################# CORS #############################
################################################################

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'application.lxc.pic.brasserie-du-slalom.fr/', 'application.lxc.pic.brasserie-du-slalom.fr',
    'https://application.lxc.pic.brasserie-du-slalom.fr', 'https://application.lxc.pic.brasserie-du-slalom.fr/',
    'dev.lxc.pic.brasserie-du-slalom.fr/api/admin/login/?next=/api/admin/',
    'dev.lxc.pic.brasserie-du-slalom.fr/api/admin/', 'dev.lxc.pic.brasserie-du-slalom.fr', '127.0.0.1:8000',
    '128.0.0.1:8000/'
]

CORS_REPLACE_HTTPS_REFERER = True

################################################################
############################# LDAP #############################
################################################################

AUTH_LDAP_SERVER_URI = "ldap://192.168.101.12:389"

AUTH_LDAP_BIND_DN = "cn=Administrator,cn=Users,dc=lxc,dc=pic,dc=brasserie-du-slalom,dc=fr"
AUTH_LDAP_BIND_PASSWORD = "P@ssword01!"

AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email": "mail"}

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=lxc,dc=pic,dc=brasserie-du-slalom,dc=fr", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"
)

################################################################
############################## JWT #############################
################################################################

JWT_AUTH = {
    'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_SECRET_KEY': 'SECRET_KEY',
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=15),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,
}

################################################################
############################# MEDIA ############################
################################################################

MEDIA_URL = 'media/'
if os.getenv('ENVIRONMENT') == 'DEV':
    MEDIA_ROOT = os.path.join(BASE_DIR, '../media/')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

if 'pytest' in sys.argv:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

################################################################
############################# EMAIL ############################
################################################################
if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/app-messages'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'No-Reply <no-reply@pic.brasserie-du-slalom.fr>'