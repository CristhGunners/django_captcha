from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import *

urlpatterns = patterns('',
	url(r'^$',  Home.as_view() , name='home'),
    url(r'^pregunta/add/$',  Pregunta_Nueva.as_view() , name='preguta_nueva'),
    url(r'^pregunta/detalle/(?P<pk>\d+)/$',  Pregunta_Detalle.as_view() , name='pregunta_detalle'),
)