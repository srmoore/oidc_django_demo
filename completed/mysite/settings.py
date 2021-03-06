"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e2+@yalgrfjpv$*au(&2$c-*sl@3_#e)o=)n5*%wzsvs7cn#o!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangooidc',
    'simpleapp'
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DEFINE AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'djangooidc.backends.OpenIdConnectBackend'
]

# Set LOGIN_URL (for django oidc)
LOGIN_URL = '/openid/openid/mitreid'

###############################################################################
# PyOIDC specific settings

# Check certificates? True by default.
# OIDC_VERIFY_SSL = True

# By default an internal user will be created for each new user that has successfully authenticate with OIDC.
# This can be disabled by setting this variable to False - in that case users must be manually referenced.
# OIDC_CREATE_UNKNOWN_USER = False

# The view for OIDC login uses a default template - it can be overridden here
# OIDC_LOGIN_TEMPLATE = "djangooidc/login.html"

# You may want to disable client registration. In that case, only the OP inside OIDC_PROVIDERS will be available.
OIDC_ALLOW_DYNAMIC_OP = False

# Information used when dynamically registering a client on an OP.
# Ignored if auto registration is not used. May also be directly reused in OIDC_PROVIDERS (as this data may be
# the same for all OPs)
# OIDC_DYNAMIC_CLIENT_REGISTRATION_DATA = {
#    "application_type": "web",
#    "contacts": ["ops@example.com"],
#    "redirect_uris": ["http://localhost:8000/openid/callback", ],
#    "post_logout_redirect_uris": ["http://localhost:8000/", ]
# }

# Default is using the 'code' workflow, which requires direct connectivity from website to the OP.
OIDC_DEFAULT_BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "profile", "email", "address", "phone"],
}

# The keys in this dictionary are the OPs (OpenID Providers) short user friendly name not the issuer (iss) name.
OIDC_PROVIDERS = {
    "mitreid": {
        "srv_discovery_url": "https://mitreid.org/",
        "behaviour": OIDC_DEFAULT_BEHAVIOUR,
        "client_registration": {
            "client_id": "f5458edf-5163-4b3b-a965-577922719fb1",
            "redirect_uris": ["http://localhost:8000/openid/callback/login/"],
            'token_endpoint_auth_method': ['private_key_jwt'],
            "enc_kid": "rsa_test",
            "keyset_jwk_file": "file://keys/keyset.jwk"
        }
    }
}

# Test OP - webfinger supported on non-standard URL, no client self registration.
# "Azure Active Directory": {
#     "srv_discovery_url": "https://sts.windows.net/9019caa7-f3ba-4261-8b4f-9162bdbe8cd1/",
#     "behaviour": OIDC_DEFAULT_BEHAVIOUR,
#     "client_registration": {
#         "client_id": "0d21f6d8-796f-4879-a2e1-314ddfcfb737",
#         "client_secret": "6hzvhNTsHPvTiUH/GUHVsFDt8b0BajZNox/iFI7iVJ8=",
#         "redirect_uris": ["http://localhost:8000/openid/callback/login/"],
#         "post_logout_redirect_uris": ["http://localhost:8000/openid/callback/logout/"],
#     }
# },
# # No webfinger support, but OP information lookup and client registration
# "xenosmilus": {
# "srv_discovery_url": "https://xenosmilus2.umdc.umu.se:8091/",
# "client_info": ME,
# "behaviour": BEHAVIOUR
# },
# # Supports OP information lookup but not client registration
# "op.example.org": {
# "srv_discovery_url": "https://example.org/op/discovery_endpoint",
# "client_registration": {
# "client_id": "abcdefgh",
# "client_secret": "123456789",
#         "redirect_uris": ["https://rp.example.com/authn_cb"],
#     }
# },
# # Does not support OP information lookup but dynamic client registration
# "noop.example.com": {
#     "provider_info": {
#         "issuer": "",
#         "authorization_endpoint": "",
#         "token_endpoint": "",
#         "userinfo_endpoint": "",
#         "registration_endpoint": "",
#         "jwks_uri": "",
#         "scopes_supported": "",
#         "response_types_supported": "",
#         "subject_types_supported": "",
#         "id_token_signing_alg_values_supported": "",
#         "claims_supported": "",
#     },
#     "client_info": ME,
# },
# # Does not support any dynamic functionality
# "nodyn.example.com": {
#     "provider_info": {
#         "issuer": "",
#         "authorization_endpoint": "",
#         "token_endpoint": "",
#         "userinfo_endpoint": "",
#         "registration_endpoint": "",
#         "jwks_uri": "",
#         "scopes_supported": "",
#         "response_types_supported": "",
#         "subject_types_supported": "",
#         "id_token_signing_alg_values_supported": "",
#         "claims_supported": "",
#     },
#     "client_registration": {
#         "client_id": "abcdefg",
#         "client_secret": "123456789",
#         "redirect_uris": ["https://rp.example.com/authn_cb"],
#     }
# },

#
###############################################################################


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
