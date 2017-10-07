from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^follow/(?P<user_id>[0-9]+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<user_id>[0-9]+)/$', views.unfollow, name='unfollow'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.homepage, name='profile'),
    url(r'^$', views.homepage, {'user_id': None,
                                'active': True}, name='homepage'),
]
