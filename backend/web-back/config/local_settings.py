import os
from .settings import *

DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('SECRET_KEY')
