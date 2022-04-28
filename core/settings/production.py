from .base import *
import django_heroku

STATIC_ROOT = BASE_DIR / 'staticfiles'

django_heroku.settings(locals())