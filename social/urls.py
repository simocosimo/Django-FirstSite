from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^profile/([0-9]+)/$', views.detail_view, name='profile'),
    url(r'', views.homepage, name='homepage'),
]
