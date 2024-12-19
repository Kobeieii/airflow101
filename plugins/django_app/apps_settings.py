import os
from pathlib import Path

ENV = os.getenv("ENV", "dev")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-fdlu#ta6#oit+usq)(1$48webd49)*gue+awvvwvj6#j%xxq9g"

SECRET_TOKEN = "m@zcJa#@5YhmoiBQMoyBizY^eiuipJ9bVO288gg^c%NhBIFqE@DHm1^*jO0Imc%J"

DEBUG = ENV == "dev"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_app.apps",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app" if (ENV == "prod") else "app_dev",
        "USER": os.getenv("MYSQL_USER", "root"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD", "airflow"),
        "HOST": os.getenv("MYSQL_HOST", "mysql"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "TIME_ZONE": "Asia/Bangkok",
        "CONN_MAX_AGE": 3600 * 2,
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Bangkok"

USE_I18N = False

USE_L10N = False

USE_TZ = True

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
        "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING"),
    },
}

