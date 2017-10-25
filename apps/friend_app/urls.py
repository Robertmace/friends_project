######## Second APP #####
from django.conf.urls import url
from . import views
from ..login_app.models import User

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^showFriend/(?P<id>\d+)$', views.showFriend),
    url(r'^addFriend/(?P<id>\d+)$', views.addFriend),
    url(r'^remFriend/(?P<id>\d+)$', views.remFriend),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
]
