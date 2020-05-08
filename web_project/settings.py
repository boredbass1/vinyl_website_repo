"""
Django settings for web_project project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'hzpe55l6azj)6*%-l+=3qx7j#3z+tkqvi!7ydf*x_ucdr!biyn'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'hzpe55l6azj)6*%-l+=3qx7j#3z+tkqvi!7ydf*x_ucdr!biyn')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'chartjs',
    'website',
    'stdimage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [r'C:\Users\Brandon Dore\Desktop\Vinyl Website\website\templates'],
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


WSGI_APPLICATION = 'web_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

ADMINS = (
    ('Brandon Dore', 'sanjohn2009@gmail.com'), # Sets me as the email admin
)

MANAGERS = ADMINS

MAILER_EMAIL_BACKEND = 'django_libs.test_email_backend.EmailBackend' # Utilises the django email backend
TEST_EMAIL_BACKEND_RECIPIENTS = ADMINS

FROM_EMAIL = ADMINS[0][1] # Tells google what email will be used
EMAIL_SUBJECT_PREFIX = 'Password Reset' # Sets the reset email subject

EMAIL_HOST = 'smtp.gmail.com' # Sets the host as gmails SMTP servers
EMAIL_HOST_USER = FROM_EMAIL

EMAIL_HOST_PASSWORD = 'vvuhpepxgwjjtynz' # Google generated app password
EMAIL_USE_TLS = True
EMAIL_PORT = 587

STATIC_URL = '/static/' # Gives django the root to the static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/' # Re-directs the user away from admin page to the home page after logging out

MEDIA_URL = '/media/' # Gives django the link to media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

