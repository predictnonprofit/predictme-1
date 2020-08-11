"""
Django settings for predict_me_project project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xdr3k(sy^bog(0#(a$&+1%zqa4$b(97qzu^3w8(x)9f4j!3_1i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG is True:
    ALLOWED_HOSTS = ["127.0.0.1", "predictme2.herokuapp.com"]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Application definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares_app.middleware.simple_middleware',
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "django.contrib.sites",
    'django.contrib.staticfiles',
    "middlewares_app.apps.MiddlewaresAppConfig",
    'widget_tweaks',
    # "data_handler.apps.DataHandlerConfig",
    "django_extensions",
    "django_countries",
    "admin_profile",
    "users.apps.UsersConfig",
    "predict_me",
    "dashboard",
    "dash_users",
    "invoice_app",
    "messages_app",
    "data_handler_admin",
    "reports_app",
    "members_app",
    "site_settings",
    "membership",
    "activity_app",
    "predictme_context_processors",
    "data_handler.apps.DataHandlerConfig",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',

]

ROOT_URLCONF = 'predict_me_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(BASE_DIR, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "maintenance_mode.context_processors.maintenance_mode",
                "predictme_context_processors.context_processors.return_all_context",
            ],
        },
    },
]

WSGI_APPLICATION = 'predict_me_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
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
AUTH_USER_MODEL = 'users.Member'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = '/static/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOGIN_URL = "login"
# LOGOUT_REDIRECT_URL = "dashboard"
LOGIN_REDIRECT_URL = "profile-overview"
LOGOUT_REDIRECT_URL = "login"
# LOGOUT_URL = "login"

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# password reset timeout days
PASSWORD_RESET_TIMEOUT_DAYS = 1

# set stripe keys
if DEBUG:
    # for test data
    # STRIPE_PUBLISHABLE_KEY = ''
    # STRIPE_SECRET_KEY = ''
    MAILER_EMAIL_BACKEND = EMAIL_BACKEND
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_SSL = False
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    # DEFAULT_FROM_EMAIL = "contact@predictme.com"
else:
    # for production
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''

# Maintenance mode configurations
# the template that will be shown by the maintenance-mode page
MAINTENANCE_MODE_TEMPLATE = '503.html'

# list of urls that will not be affected by the maintenance-mode
# urls will be used to compile regular expressions objects
MAINTENANCE_MODE_IGNORE_URLS = ("dashboard-url")

# deploy tips
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# SITE_ID = 4

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# fix Error 400: redirect_uri_mismatch
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"


#### Sessions config ###
SESSION_EXPIRE_SECONDS = 5120  # 5 Mins
# SESSION_EXPIRE_SECONDS = 10  # 20 Sec
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_TIMEOUT_REDIRECT = 'login'

