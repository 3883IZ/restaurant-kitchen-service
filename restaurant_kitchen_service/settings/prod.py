from .base import *
import os

# Продакшн режим
DEBUG = False

# Дозволені хости
ALLOWED_HOSTS = []
hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if hostname:
    ALLOWED_HOSTS.append(hostname)
else:
    # fallback, якщо змінна не задана
    ALLOWED_HOSTS = ["restaurant-kitchen-service.onrender.com"]

# WhiteNoise для статичних файлів
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# База даних (Neon через Render env vars)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_DB_PORT"),
    }
}

# Статика
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media на Render Disk
MEDIA_URL = "/media/"
MEDIA_ROOT = "/media"

# Логування для відображення помилок у Render Logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",  # у продакшн краще INFO, щоб не засмічувати логи
    },
}
