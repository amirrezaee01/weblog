from mysite.settings import *

# Development-specific settings
SECRET_KEY = 'django-insecure-my^xk1b6@oj#bj!p0y5&lul1q%ai$%7wqi5mx&4@#7j5)ehc@+'
DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [BASE_DIR / "statics"]

# Django Compressor settings for development
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

X_FRAME_OPTIONS = "SAMEORIGIN"
