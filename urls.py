from django.conf.urls import url
from . import views

                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^registration$', views.display_registration),
    url(r'^registration/create$', views.regisration_create),
    url(r'^homepage$', views.home_page),
    url(r'^homepage/point_of_view$', views.point_of_view),
    url(r'^homepage/info$', views.homepage_info),
    url(r'^homepage/video$', views.homepage_video),
    url(r'^homepage/details/(?P<id>\d+)$', views.homepage_details),
    url(r'^homepage/delete/(?P<id>\d+)$', views.homepage_delete),
    url(r'^homepage/added/(?P<id>\d+)$', views.homepage_added),
    url(r'^homepage/update/(?P<id>\d+)$', views.homepage_update),
    url(r'^homepage/edit/(?P<id>\d+)$', views.homepage_edit),
    url(r'^homepage/like/(?P<id>\d+)$', views.homepage_like),

    url(r'^logout$', views.logout)

]