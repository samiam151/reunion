from django.conf.urls import include, url
from django.contrib import admin

from .import views

urlpatterns = [
    url(r'^$', views.rsvp_list, name="list"),
    url(r'^add$', views.RSVPCreate.as_view(), name="add"),
    url(r'^delete/(?P<pk>\d+)', views.rsvp_delete, name="delete")
]