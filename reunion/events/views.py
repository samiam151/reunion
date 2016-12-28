from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers

from .models import Event

# Event Home
def eventsHome(request):
    events = Event.objects.all()
    return render(request, "events/home.html", {"events": events})

# Event Detail
def eventsDetail(request, pk=None):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {"event": event})

# RESTful Endpoint for all Events
def json_events_all(request):
    events = Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data, content_type="applcations/json")