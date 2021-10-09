"""
WSGI config for userMeasurement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv('settings.env')
setting = os.environ.get('ENV_NAME')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'userMeasurement.settings.{setting}')

application = get_wsgi_application()
