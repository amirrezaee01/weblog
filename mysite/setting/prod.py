from mysite.settings import *

# Production-specific settings
SECRET_KEY = 'django-insecure-my^xk1b6@oj#bj!p0y5&lul1q%ai$%7wqi5mx&4@#7j5)ehc@+'
DEBUG = False

ALLOWED_HOSTS = ["amirrezaee.ir", "www.amirrezaee.ir"]
SITE_ID = 2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / '/home/amirrez2/public_html/static'
MEDIA_ROOT = BASE_DIR / '/home/amirrez2/public_html/media'
STATICFILES_DIRS = [BASE_DIR / "statics"]

# Enable compression in production
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

# Security settings
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "SAMEORIGIN"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = False  # Configure in web server
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'
