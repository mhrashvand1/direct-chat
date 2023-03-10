from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="xfdgr45gvtj678cerxx")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False)

def parse_list_cast(value):
    if type(value) == str:
        return [i.strip() for i in value.split()]
    elif type(value) in [list, tuple]:
        return [i.strip() for i in value]
    else:
        return value
    
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=parse_list_cast,
    default=["*"]
)

INTERNAL_IPS = config(
    "INTERNAL_IPS",
    cast=parse_list_cast,
    default=["*"]
)


# Application definition
INSTALLED_APPS = [
    # Dephne
    "daphne",
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    # Third party packages
    'channels',
    'django_cleanup.apps.CleanupConfig',
    # Project app
    'account.apps.AccountConfig',
    'core.apps.CoreConfig',
    'activity.apps.ActivityConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default="directchat"),
        "USER": config("DB_USER", default="directchat"),
        "PASSWORD": config("DB_PASSWORD", default="directchat"),
        "HOST": config("DB_HOST", default="postgres"),
        "PORT": config("DB_PORT", default=5432),
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

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / 'static'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# User Model
AUTH_USER_MODEL = 'account.User'

# channels
ASGI_APPLICATION = 'config.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    config("REDIS_HOST", default="redis"),
                    config("REDIS_PORT", default="6379")
                )
            ],
        },
    },
}
