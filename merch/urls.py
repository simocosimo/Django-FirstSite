from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([0-9]+)/$', views.merch_detail, name='merch_detail'),
    url(r'^([0-9]+)/([0-9]+)/$', views.merch_detail, name='merch_detail'),
]