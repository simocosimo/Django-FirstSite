from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^profile/([0-9]+)/$', views.homepage, name='profile'),
    url(r'', views.homepage, {'user_id': None,
                              'active': True}, name='homepage'),
]
