from django.conf.urls import include, url
from apps.cita.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^panel/$', login_required(panel), name='panel'),
    url(r'^documentacion/$', login_required(documentacion), name='documentacion'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^citas/$', login_required(lista_citas), name='lista_citas'),
    url(r'^citas/agregar/$', login_required(agregar_cita), name='agregar_cita'),
    url(r'^citas/editar/(?P<id_cita>[\d{1,9}]+)/$', login_required(editar_cita), name='editar_cita'),
    url(r'^citas/eliminar/(?P<id_cita>[\d{1,9}]+)/$', login_required(eliminar_cita), name='eliminar_cita'),
]