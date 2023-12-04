from .base import *

SECRET_KEY = "j&8vqzrt_9-bngny95u2mu*gsfdu8%f*h5tl=c*qit_oa9h0r+"

DEBUG_MODE=False

ALLOWED_HOSTS=['localhost','127.0.0.1','0.0.0.0','codejunior.fly.dev']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8069','https://codejunior.fly.dev']

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'defaultdb',
    'USER': 'doadmin',
    'PASSWORD': 'AVNS_-cGTNpKh6BoKtJFuvd6',
    'HOST': 'db-postgresql-nyc3-95528-do-user-8907006-0.c.db.ondigitalocean.com',
    'PORT': '25060',
  }
}