from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addmerch/(?P<user_id>[0-9]+)/(?P<merch_id>[0-9]+)/', views.add_merch,
        name='add_merch'),
    url(r'^rmmerch/(?P<user_id>[0-9]+)/(?P<merch_id>[0-9]+)/', views.rm_merch,
        name='remove_merch'),
    url(r'^(?P<type>[0-9]+)/$', views.merch_detail, name='merch_list'),
    url(r'^(?P<type>[0-9]+)/(?P<merch_id>[0-9]+)/$', views.merch_detail,
        name='merch_detail'),
]
