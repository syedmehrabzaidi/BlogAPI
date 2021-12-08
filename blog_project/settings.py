import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b$tu81h+d$ozb(ctsj!tq#7@!!65gf-x-(_ab@l*fzp%)4mo++'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 3rd-party apps
    'rest_framework',
    'wkhtmltopdf',
    'djoser',
    'celery',
    'django_filters',

    # Local
    'posts.apps.PostsConfig',
    'accounts.apps.AccountsConfig',
    'blog.apps.BlogConfig',
    'profiles.apps.ProfilesConfig',

]

ALLOWED_HOSTS = ['*']

# Application definition


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1  # new

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',),

    'DEFAULT_FILTER_BACKENDS': (
         'django_filters.rest_framework.DjangoFilterBackend',
    ),

}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

AUTH_USER_MODEL = 'profiles.ProfileCustomUser'

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

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'blog_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'blog_user',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd6dtrkcj423499',
#         'USER': 'hdyxkruxtqdgzh',
#         'PASSWORD': '2ba8bae4e68002b8ab02047cada3e5c4bb077a60c36a7e7c1ad29947a4a3c536',
#         'HOST': 'ec2-34-198-189-252.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }

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

# blogapi_change bd final (custom model)
STATIC_ROOT = '/static/'
STATIC_URL = "/static/"
django_heroku.settings(locals())

STATICFILES_DIRS = [
    BASE_DIR, "static",

]

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

CELERY_BROKER_URL = 'amqp://localhost'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# add your host of the email here in this case its Gmail so we are going to use Gmail host
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
# add the port number of the email server
EMAIL_PORT = 587
# add your gamil here
EMAIL_HOST_USER = 'Mehrab@gmail.com'
# add your password here
EMAIL_HOST_PASSWORD = 'Mehrab123'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = 'blog4/media'
MEDIA_URL = '/media/'

WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': False,
}

