"""
Django settings for wsdProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_PATH = os.path.realpath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'db.sqlite3')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #"/home/mukhera3/Desktop/wsdProject/gamestore/templates",  #TODO use absolute path here

)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lth8)*_jkh+_lou&#p0=jaw1jfb=u=#ky=w!0cq(pxt6l^zc#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gamestore',
#    'django_facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.debug',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    'django.core.context_processors.static',
#    'django.core.context_processors.tz',
#    'django.core.context_processors.request',
#    'django.contrib.messages.context_processors.messages',
#    'django_facebook.context_processors.facebook',
#)
#AUTHENTICATION_BACKENDS = (
#    'django_facebook.auth_backends.FacebookBackend',
#    'django.contrib.auth.backends.ModelBackend',
#)
#AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile',

# Django console backend for e-mail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROOT_URLCONF = 'wsdProject.urls'

WSGI_APPLICATION = 'wsdProject.wsgi.application'

#FACEBOOK_APP_ID= '642071779255664'
#FACEBOOK_APP_SECRET='210b190eda807f802213aa06b97d16f8'
#FACEBOOK_EXTENDED_PERMISSIONS =['email']
#LOGIN_REDIRECT_URL='/'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

if "DYNO" in os.environ:
    #DEBUG = False
    ALLOWED_HOSTS = ['*']    
    STATIC_ROOT = 'staticfiles'
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()
