from .staging import *


# Allowed hosts for the site
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['{{ cookiecutter.live_hostname }}'])

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('SITE_URL', default='https://{{ cookiecutter.live_hostname }}')
DJANGO_SITE_URL = env.str('DJANGO_SITE_URL', default=SITE_URL)

EMAIL_HOST_PASSWORD = 'TODO (api key)'

RAVEN_BACKEND_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG = {'dsn': RAVEN_BACKEND_DSN}

# CORS overrides
CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
