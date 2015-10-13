"""
Django settings for qexx project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%u35k$aq4@icwqiqkr5$msq7w*=ox3=mji@3*ankxa@47pv^k&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
ADMINS = (('Sergey Borisov', 'sborisov@ardushop.ru',),)


# Application definition

INSTALLED_APPS = (
    'autocomplete_light',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'haystack',
    'mptt',
    'widget_tweaks',
    'mathfilters',
    'easy_thumbnails',
    'common',
    'accounts',
    'products',
    'cart',
    'coupons',
    'payment',
    'ratings',
    'shipping',
    'orders',
    'stock',
    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'qexx.urls'

WSGI_APPLICATION = 'qexx.wsgi.application'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_production')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Модель пользователей и авторизации

AUTH_USER_MODEL = 'accounts.UserProfile'
AUTHENTICATION_BACKENDS = ('accounts.backends.MyModelBackend',)

# Процессор шаблонов

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('cart.context_processors.user_cart',
                                'common.context_processors.current_site')

# Медиа файлы

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Настройки email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
if DEBUG:
    # На дев-сервере будем отправлять почту в консоль
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Thumbnail-ы
THUMBNAIL_ALIASES = {
    '': {
        # Превьюшки для товаров в каталоге
        'product_preview': {'size': (150, 150),
                            'background': (255, 255, 255)},
        # Превьюшка для основного изображения на странице товара
        'product_preview_main': {'size': (250, 250),
                                 'background': (255, 255, 255)},
        # Превьюшки для остальных изображений на странице товара
        'product_preview_small': {'size': (85, 85),
                                  'background': (255, 255, 255)},
    },
}

# Настройки поиска
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# Обратный адрес почты
EMAIL_REPLY = 'no-reply@qexx.ru'

# Доставка
SHIPPING_CLASSES = (
    'shipping.methods.pickup_delivery',
    'shipping.methods.local_delivery',
    'shipping.methods.post_delivery'
)

# Оплата
PAYMENT_CLASSES = (
    'payment.gateways.cash',
    'payment.gateways.cash_on_delivery',
    'payment.gateways.robokassa'
)