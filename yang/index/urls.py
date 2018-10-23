from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$',login_views),
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^upload/$',upload_views),
    url(r'^share/$',share_views),
    url(r'^open/$',open_views),
    url(r'^download/$',download_views),
    ]