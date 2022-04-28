from .base import *
import django_heroku
import os

SECRET_KEY = os.getenv('SECRET_KEY')

STATIC_ROOT = BASE_DIR / 'staticfiles'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.environ.get('REDIS_URL', 'redis://localhost:6379')]
        }
    }
}

CHACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

django_heroku.settings(locals())