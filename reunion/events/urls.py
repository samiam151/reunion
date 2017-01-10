from django.conf.urls import include, url

from .import views

urlpatterns = [
    url(r'^$', views.eventsHome, name='home'),
    url(r'^(?P<pk>\d+)$', views.eventsDetail, name='detail'),
    url(r'^json_events_all$', views.json_events_all, name='json-events-all'),
]