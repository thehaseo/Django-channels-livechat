from .base import *
import django_heroku
import os

SECRET_KEY = os.getenv('SECRET_KEY')

STATIC_ROOT = BASE_DIR / 'staticfiles'

ALLOWED_HOSTS = ['localhost', 'channels-livechat.herokuapp.com']

ASGI_APPLICATION = 'core.routing.application'

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

CSRF_TRUSTED_ORIGINS = ['https://channels-livechat.herokuapp.com', 'localholst']

django_heroku.settings(locals())
