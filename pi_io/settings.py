# Django settings for rpi_websocket

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Hiye Shin', 'hiyeshin@gmail.com')
)

MANAGERS = ADMINS

# below database should be adjusted later
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',    # but it can be hooked with heroku toooooooo!
		'NAME': 'I want to use mongoDB', # because I want to 
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': ''
	}
}


TIME_ZONE = 'American/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True # format dates, numbers and such for the current locale setup
USE_TZ = True
MEDIA_ROOT = "/Users/Hazel/movies" # it should be an absolute path

MEDIA_URL = '/media'

STATIC_ROOT = '/home/desktop/yoga_site/www/static/'

STATICFILES_DIRS = (
 # there should be some absolute path
)


STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finder.DefaultStroageFinder',
	'compressor.finders.CompressorFinder',
)

SECRET_KEY = 'somethingrandomhere'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleWare',
	'django.middleware.csrf.CsrfViewMiddleWare',
	'django.contrib.auth.middleware.MessageMiddleware',
	'django.contrib.message.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pi_io.urls'

# python dotted path to the WSGI application used by django's runserever
WSGI_APPLICATION = 'pi_io.wsgi.application'

TEMPLATE_DIRS = (
	"/Users/Hazel/Desktop/yoga_site/templates" #I need to change to the absolute path later
)

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmen.LocMemCache',
	}
}


INSTALLED_APPS = (
	'django.contrib.auth', # authentification system
	'django.contrib.contenttypes', # framework for content type
	'django.contrib.sessions', # session framework
	'django.contrib.sites', # framework for multiple sites with one django installation
	'django.contrib.messages',
	'django.contrib.staticfiles', # static file management framework
	'django.contrib.admin',
	'compressor',
	'pi_io_site',
	'ws_comm',
)

# beginning it will be false
COMPRESS_ENABLED = False

COMPRESS_PRECOMPILERS = ( # what if I don't want to use less? what does this for? I am not gonna use it
	('text/less', 'lessc {infile} {outfile}'), # I will change this later
)


COMPRESS_CSS_FILTERS = (
	'compressor.filters.css_default.CssAbsoluteFilter',
	'compressor.filters.cssmin.CSSMinFilter',
)

# below will be a sample logging configuration
# the only tangible logging performed by this configuration is to send an email to the sites
# well do I need this?

LOGGING = {
	'version': 1,
	'disable_existing_loggers':False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.ReqioreDebigFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
		'handlers': ['mail_admins'],
		'level': 'ERROR',
		'propagate': True,
		},
	}
}


WS_SERVER_IP = '0.0.0.0'
WS_SERVER_HTTP = 8000
WS_SERVER_HTTP_SSL = False