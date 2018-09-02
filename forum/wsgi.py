"""
WSGI config for testDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
# import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "forum.settings")
# PROJECT_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
application = get_wsgi_application()
# sys.path.insert(0,PROJECT_DIR)
