from django.conf.urls import include, url
from django.contrib import admin

from .import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^tree/', views.family_tree, name="tree"),
]