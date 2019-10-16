"""
Django settings for projet_ka project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b)*jr9tz$u)j!0wk+*ijj+v85%)2e&c08^^rya!zq#v=3)u+2!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # True uniquement DEV

ALLOWED_HOSTS = ['51.77.203.171', '*'] # '*' uniquement DEV


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'boutique',
    'pages',
    'gunicorn',
    'django_filters',
    'users',
]

# Update du modèle d'identification pour USER : modèle 'MyUser' dans l'app 'users'

AUTH_USER_MODEL = 'users.MyUser'

LOGIN_URL = '/users/login/'

LOGIN_REDIRECT_URL = '/users/profile/'

LOGOUT_REDIRECT_URL = None

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projet_ka.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # cette ligne ajoute le dossier templates/ à la racine du projet
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

WSGI_APPLICATION = 'projet_ka.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test2',
        'USER': 'kous',
        'PASSWORD': 'motdepasse',
        'HOST': 'localhost',
        'PORT': '5432',
        },

    'customers': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bddclient',
        'USER': 'kous',
        'PASSWORD': 'motdepasse',
        'HOST': 'localhost',
        'PORT': '5432',
        },
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) # DEV !!
STATIC_URL = '/static/' # le plus important pour le dev / adresse pour servir les fichiers statiques DEV # DEV et PROD

#MEDIA_URL = '/media/' # En développement pour le chargement des images serveur

#STATIC_ROOT = os.path.join(BASE_DIR, 'static/') # PROD !!

STATIC_ROOT = os.path.join(PROJECT_ROOT,'static') # DEV !!

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
] #Optionnel, uniquement pour le dev A SUPPRIMER en prod !!

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # Pour la prod, debug: False
MEDIA_URL = '/media/'
