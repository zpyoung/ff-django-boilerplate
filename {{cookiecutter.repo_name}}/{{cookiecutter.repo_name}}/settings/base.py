"""
Django settings for {{cookiecutter.project_title}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

import environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(SITE_ROOT, ...)
SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = environ.Path(SITE_ROOT)


# Load env to get settings
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    # By default use django.env file from project root directory
    env.read_env(str(ROOT_DIR.path('django.env')))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ADMINS = (
    ('Admins', '{{ cookiecutter.admin_email }}'),
)
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = '[{{cookiecutter.project_title}}] '  # subject prefix for managers & admins

SESSION_COOKIE_NAME = '{{ cookiecutter.repo_name }}_ssid'
SESSION_SAVE_EVERY_REQUEST = True  # Set cookie headers on every request - This is for api
SESSION_COOKIE_DOMAIN = env.str('SESSION_COOKIE_DOMAIN', default=None)
CSRF_COOKIE_DOMAIN = SESSION_COOKIE_DOMAIN


INSTALLED_APPS = [
    # Local apps
    'accounts',
    '{{cookiecutter.repo_name}}',
{%- if cookiecutter.include_cms == 'yes' %}

    # CMS apps
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'djangocms_admin_style',
    'reversion',
    'easy_thumbnails',
    'filer',
    'mptt',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_text_ckeditor',
{%- endif %}

    # Third-party apps
    'rest_framework',
    'django_filters',
    'tg_react',
    'crispy_forms',
    'corsheaders',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
{%- if cookiecutter.include_cms == 'yes' %}
    'django.contrib.sites',
{%- endif %}
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    {%- if cookiecutter.include_cms == 'yes' %}
    'cms.middleware.utils.ApphookReloadMiddleware',
    {%- endif %}
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    {%- if cookiecutter.include_cms == 'yes' %}
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    {%- endif %}
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                {%- if cookiecutter.include_cms == 'yes' %}
                'django.template.context_processors.csrf',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                {%- endif %}
            ],
        },
    },
]
{%- if cookiecutter.include_cms == 'yes' %}

THUMBNAIL_PROCESSORS = (
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
)

CMS_TEMPLATES = (
    ('cms_main.html', 'Main template'),
)
{%- endif %}


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('DATABASE_HOST', default='postgres'),
        'PORT': env.int('DATABASE_PORT', default=5432),
        'NAME': env.str('DATABASE_NAME', default='the_platform'),
        'USER': env.str('DATABASE_USER', default='the_platform'),
        'PASSWORD': env.str('DATABASE_PASSWORD', default='the_platform'),
    }
}


# Redis config (used for caching{% if cookiecutter.include_celery == 'yes' %} and celery{% endif %})
REDIS_HOST = env.str('REDIS_HOST', default='redis')
REDIS_PORT = env.int('REDIS_PORT', default=6379)
REDIS_DB = env.int('REDIS_DB', default=1)
REDIS_URL = env.str('REDIS_URL', default='redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB))
{%- if cookiecutter.include_celery == 'yes' %}


# Celery configuration
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_REDIS_CONNECT_RETRY = True
CELERYD_HIJACK_ROOT_LOGGER = False
BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True}

CELERY_TIMEZONE = 'UTC'

# Set your Celerybeat tasks/schedule here
CELERYBEAT_SCHEDULE = {
    'default-task': {
        # TODO: Remove the default task after confirming that Celery works.
        'task': '{{cookiecutter.repo_name}}.tasks.default_task',
        'schedule': 5,
    },
}
{%- endif %}


# Caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
    ('et', 'Eesti keel'),
)
LOCALE_PATHS = (
    'locale',
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files and media (CSS, JavaScript, images)
MEDIA_ROOT = '/files/media'
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

STATIC_ROOT = '/files/assets'
STATIC_URL = env.str('STATIC_URL', default='/static/')

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default='dummy key')

AUTH_USER_MODEL = 'accounts.User'

# Static site url, used when we need absolute url but lack request object, e.g. in email sending.
SITE_URL = env.str('SITE_URL', default='http://127.0.0.1:8000')
DJANGO_SITE_URL = env.str('DJANGO_SITE_URL', default='http://127.0.0.1:3000')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['django', 'localhost', '127.0.0.1'])


{%- if cookiecutter.include_cms == 'yes' %}

SITE_ID = 1
{%- else %}

# Don't allow site's content to be included in frames/iframes.
X_FRAME_OPTIONS = 'DENY'
{%- endif %}


ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'


# Crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Email config
DEFAULT_FROM_EMAIL = "{{cookiecutter.project_title}} <info@{{ cookiecutter.live_hostname }}>"
SERVER_EMAIL = "{{cookiecutter.project_title}} server <server@{{ cookiecutter.live_hostname }}>"

# Show emails in the console, but don't send them.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SMTP  --> This is only used in staging and production
EMAIL_HOST = env.str('EMAIL_HOST', default='smtp.sparkpostmail.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='SMTP_Injection')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', default='')


# Base logging config. Logs INFO and higher-level messages to console. Production-specific additions are in
#  production.py.
#  Notably we modify existing Django loggers to propagate and delegate their logging to the root handler, so that we
#  only have to configure the root handler.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)d %(funcName)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {'handlers': [], 'propagate': True},
        'django.request': {'handlers': [], 'propagate': True},
        'django.security': {'handlers': [], 'propagate': True},
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Disable a few system checks. Careful with these, only silence what your really really don't need.
# TODO: check if this is right for your project.
SILENCED_SYSTEM_CHECKS = [
    'security.W001',  # we don't use SecurityMiddleware since security is better applied in nginx config
]


# Rest framework configuration
REST_FRAMEWORK = {
    # Disable Basic auth
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # Change default full-url media files to be only stored path, needs /media prepended in frontend
    'UPLOADED_FILES_USE_URL': False,
}


# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Default values for sentry
RAVEN_BACKEND_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO:TODO@sentry.thorgate.eu/TODO')
RAVEN_PUBLIC_DSN = env.str('RAVEN_BACKEND_DSN', default='https://TODO@sentry.thorgate.eu/TODO')
RAVEN_CONFIG = {'dsn': RAVEN_BACKEND_DSN}
