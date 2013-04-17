from django.conf.urls import patters, include, url

urlpatters = patters('',
	url(r'^rpis/$', 'user_api.vies.rpi_list'),
)