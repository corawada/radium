import os
from .settings import *

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
