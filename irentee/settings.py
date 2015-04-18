"""
Django settings for irentee project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't3cx#i^p$ra)vgpv-@u)@++$jom^jh3k3@xvj@y%qpz+hqw0f7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MANAGED=True
# Application definition
TEMPLATE_DIRS={
os.path.join(BASE_DIR,'static'),
    "irent",
    "irent/templates/Landing/",
    "irent/templates/seller/"
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'irent',
    'social_auth'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'irentee.urls'

WSGI_APPLICATION = 'irentee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'irentee',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


FACEBOOK_APP_ID  =  '472648226217533'
FACEBOOK_API_SECRET = '41bba9de5c5052cd5da01ceff396e0bc'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'static', 'static_root')

STATICFILES_DIRS=os.path.join(BASE_DIR,'static', 'static_dirs'),

MEDIA_ROOT=os.path.join(BASE_DIR,'static', 'media')

MEDIA_URL='/media/'


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend'
)