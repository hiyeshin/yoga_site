from django.conf.urls import patterns, include, url

# if we uncomment the two lines below, we can enable the admin
from django.contrib import admin
admin.autodiscover()

urlpatters = patters('',
	# below is just examples and it can be changed later
	# and it's REGULAR EXPRESSION hehehehe
	url(r'^$', 'pi_io_site.views.home', name = 'home'),
	url(r'^ws_comm/', include('ws_comm.urls')),
	url(r'^user_api/', include('user_api.urls')),
	url(r'^displays/(?P<rpi_mac>.+)$, 'pi_io_site.views.rpi_displays'),
	url(r'^admin/', include(admin.site.urls)),
)