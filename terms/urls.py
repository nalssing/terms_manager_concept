from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'publish/(?P<page_id>[0-9]+)/$', views.publish),
]
