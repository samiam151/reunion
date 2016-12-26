from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include("home.urls", namespace="home")),
    url(r'^admin/', admin.site.urls),
    url(r'^rsvp/', include("rsvp.urls", namespace="rsvp")),
    url(r'^tree/', include("tree.urls", namespace="tree")),
    url(r'^events/', include("events.urls", namespace="events")),
]
