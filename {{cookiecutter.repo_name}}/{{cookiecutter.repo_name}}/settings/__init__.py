import os
import sys


if not os.environ.get('DJANGO_PRODUCTION_MODE'):
    # When not using production mode, e.g setting DJANGO_SETTINGS_MODULE manually
    # Try using local.py
    try:
        from settings.local import *
    except ImportError:
        sys.stderr.write("Couldn't import settings.local, have you created it from settings/local.py ?\n")
        sys.exit(1)
