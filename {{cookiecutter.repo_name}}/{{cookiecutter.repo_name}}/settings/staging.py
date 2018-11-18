from corsheaders.defaults import default_headers

from .base import *


DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['{{cookiecutter.repo_name|as_hostname}}.{{cookiecutter.test_host}}'])

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('SITE_URL', default='https://{{cookiecutter.repo_name|as_hostname}}.{{cookiecutter.test_host}}')
DJANGO_SITE_URL = env.str('DJANGO_SITE_URL', default=SITE_URL)

SESSION_COOKIE_DOMAIN = env.str('SESSION_COOKIE_DOMAIN', default=None)
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default='TODO (api key)')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_URL = env.str('STATIC_URL', default='/assets/')

# Production logging - all INFO and higher messages go to info.log file. ERROR and higher messages additionally go to
#  error.log file plus to Sentry.
if env.str('DISABLE_FILE_LOGGING') != 'y':
    LOGGING['handlers'] = {
        'info_log': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/{{cookiecutter.repo_name}}/info.log',
            'formatter': 'default',
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/{{cookiecutter.repo_name}}/error.log',
            'formatter': 'default',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    }
    LOGGING['loggers'][''] = {
        'handlers': ['info_log', 'error_log', 'sentry'],
        'level': 'INFO',
        'filters': ['require_debug_false'],
    }
else:
    # When no file logging, also enable sentry
    LOGGING['loggers'][''] = {
        'handlers': ['console', 'sentry'],
        'level': 'INFO',
        'filters': ['require_debug_false'],
    }

# Sentry error logging
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
RAVEN_BACKEND_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG = {'dsn': RAVEN_BACKEND_DSN}

# CORS overrides
CORS_ORIGIN_ALLOW_ALL = False
CORS_EXPOSE_HEADERS = default_headers
CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
