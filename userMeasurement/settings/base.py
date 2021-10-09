"""
Django settings for userMeasurement project.

Generated by 'django-admin startproject' using Django 3.2.8.

"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'hj3ni5)&nansxpe(0wbmnhdea6+#g$o72own_!3&yjp56^r5_k'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'user',
    'measurement',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'userMeasurement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'userMeasurement.wsgi.application'


# Database
DATABASE_ROUTERS = ['user.router.UserRouter', 'measurement.router.MeasurementRouter', 'userMeasurement.router.PrimaryRouter']
DATABASES = {
    'default': {
        "TEST": {"NAME": "test_db",
                 'ENGINE': 'django.db.backends.postgresql',
                 },
    },
    'user_db': {
        'NAME': 'user_db',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': '123456'
    },
    'measurement_db': {
        'NAME': 'measurement_db',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': '123456'
    },
    'primary_db': {
        'NAME': 'project_db',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': '123456'
    }
}
# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# for encrypt database fields
SALT_KEY = 'QAZxsw2EDCVFR5tgbNHY&UJMkiOLp'