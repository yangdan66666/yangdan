from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^shangchuan/$',shangchuan_views),
    url(r'^gongxiang/$',gongxiang_views),
    url(r'^dakai/$',dakai_views),
    url(r'^xiazai/$',xiazai_views),
    ]