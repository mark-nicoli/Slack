from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    url(r'^output', views.output, name='output'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^select', views.select, name='select'),
    url(r'^index', views.index, name='index'),
]
