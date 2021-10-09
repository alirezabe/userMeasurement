"""
ASGI config for userMeasurement project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

load_dotenv('settings.env')
setting = os.environ.get('ENV_NAME')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'userMeasurement.settings.{setting}')

application = get_asgi_application()
