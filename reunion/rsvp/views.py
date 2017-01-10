from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
# from django.core.mail import mail_admins

from .models import RSVP

# Create your views here.
def rsvp_list(request):
    rsvps = RSVP.objects.all()

    def map_by_family():
        rsvps_by_family = []
        families = list(set([rsvp.member for rsvp in rsvps]))
        for family in families:
            people_in_family = [rsvp.name for rsvp in rsvps if rsvp.member == family]
            rsvps_by_family.append({ "name": family, "people": people_in_family })
        return rsvps_by_family

    context = {
        "rsvps": rsvps,
        "rsvps_by_family": map_by_family(),
    }

    return render(request, 'rsvp/list.html', context)

def rsvp_delete(request, pk=None):
    instance = get_object_or_404(RSVP, pk=pk)
    instance.delete()
    return redirect("rsvp:list")

class RSVPCreate(CreateView):
    model = RSVP
    fields = ['name','numGuests', 'member']
    template_name = 'rsvp/add.html'
    success_url = '/rsvp'

    def form_valid(self, form):
        mail_admins("New RSVP", "There is a new RSVP.")
        return super(RSVPCreate, self).form_valid(form)

class RSVPEdit(UpdateView):
    model = RSVP
    fields = ['name', 'numGuests', 'member']
    template_name = 'rsvp/edit.html'
    success_url = '/rsvp'

class RSVPDetail(DetailView):
    model = RSVP
    template_name = 'rsvp/detail.html'
    context_object_name = 'rsvp'

# RESTful Endpoint for RSVPs
def json_rsvp_all(request):
    rsvps = RSVP.objects.all()
    data = serializers.serialize('json', rsvps)
    return HttpResponse(data, content_type="applcations/json")