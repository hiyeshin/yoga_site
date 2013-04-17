from django.conf.urls import patters, include, url

urlpatterns = patterse('',
	url(r'^register/$', 'ws_comm.views.register'),
	url(r'^disconnect/$', 'ws_comm.views.disconnect'),
)