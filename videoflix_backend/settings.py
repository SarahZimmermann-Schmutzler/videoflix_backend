"""
Django settings for videoflix_backend project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xeodur9c8%83^@u^o#b9v00!3g-3j&gjvzhpy#d64s7boplobo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

def show_toolbar(request):    
    # für einen bestimmten User anzeigen:   
    # return not request.user.username == "Sarah"
    # Toolbar ausschalten
    return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '34.118.16.160',
    'backend.s-zimmermann-schmutzler.de',
]

CORS_ALLOW_ALL_ORIGINS = [
    'http://localhost:4200',
    'https://videoflix.s-zimmermann-schmutzler.de',
]

# CORS_ALLOW_ALL_ORIGINS = True

CACHE_TTL = 60*15

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'videoflix.apps.VideoflixConfig',
    'debug_toolbar',
    'django_rq',
    'import_export',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        # 'USERNAME': 'some-user',
        'PASSWORD': 'foobared',
        'DEFAULT_TIMEOUT': 360,
        # Eventual additional Redis connection arguments
        # 'REDIS_CLIENT_KWARGS': {    
        #     'ssl_cert_reqs': None,
        # },
    },
}

CACHES = {    
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",   
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": { 
            "PASSWORD": 'foobared',           
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "videoflix"
    }
}

ROOT_URLCONF = 'videoflix_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'videoflix_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'videoflix_DB',
        'USER': 'postgres',
        'PASSWORD': 'Post123?!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/staticfiles')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#default static files backend.s-zimmermann-schmutzler.de/videoflix
STATIC_ROOT = '/home/sarah_zimmermannschmutzler/projects/videoflix_backend/static/staticfiles'
STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
