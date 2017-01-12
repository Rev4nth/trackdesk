from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.login , name = 'login'),
        url(r'^signup/$', views.signup,name='signup'),
        url(r'^$', views.ticket_index, name="ticket_index"),
        url(r'^(?P<ticket_id>[0-9]+)/$', views.ticket_show, name='ticket_show')
]
