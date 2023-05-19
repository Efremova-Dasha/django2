"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import logging.config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger('NewsPaper.news.NewsPaper')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@=x#chn5^&$o*0q%#)unwdaf0&h=0$zhepum2e@5-%qj19^rll'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'accounts',
    'django.contrib.flatpages',
    'django_filters',
    'sign',
    'protect',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/post/'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT = '/post/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_HOST = 'smpt.yandex.ru'
EMAIL_POST = 465
EMAIL_HOST_USER = 'd.efre44'
EMAIL_HOST_PASSWORD = 'нужно создать этот файл'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ADMINS = [
    ('я опять забыла админку', 'dsavcuk921@gmail.com')
]

SERVER_EMAIL = 'd.efre44@yandex.com'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://default:wGtgIZGNUg1SSHAHdabAspeulk75qLTg@redis-11696.c74.us-east-1-4.ec2.cloud.redislabs.com:11696'
CELERY_RESULT_BACKEND = 'redis://default:wGtgIZGNUg1SSHAHdabAspeulk75qLTg@redis-11696.c74.us-east-1-4.ec2.cloud.redislabs.com:11696'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

#redis-cli -u redis://default:wGtgIZGNUg1SSHAHdabAspeulk75qLTg@
#redis-11696.c74.us-east-1-4.ec2.cloud.redislabs.com:11696

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        "for_debug_and_above": {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        "for_warning_and_above": {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
        },
        "for_critical_and_above": {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_debug_and_above'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'for_general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'for_debug_and_above',
            'filename': 'general.log',
        },
        'for_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'for_critical_and_above',
            'filename': 'errors.log',
        },
        'for_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'for_warning_and_above',
            'filename': 'security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'for_general'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['for_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['for_errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['for_errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['for_errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['for_security'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOGGING)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]