from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.template.defaultfilters import time, date

from .models import Event

# Event Home
def eventsHome(request):
    events = Event.objects.all()

    def get_events_by_day():
        events_by_day = []
        days = sorted(list(set([date(event.time_start) for event in events])))
        for day in days:
            events_that_day = [event for event in events if date(event.time_start) == day]
            events_by_day.append({ "day": day, "events": events_that_day })
        return events_by_day

    return render(request, "events/home.html", {"events": events, "events_by_day": get_events_by_day()})

# Event Detail
def eventsDetail(request, pk=None):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {"event": event})

# RESTful Endpoint for all Events
def json_events_all(request):
    events = Event.objects.all()
    data = serializers.serialize('json', events)
    return HttpResponse(data, content_type="applcations/json")