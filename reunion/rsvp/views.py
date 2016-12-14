from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import RSVP

# Create your views here.
def rsvp_list(request):
    rsvps = RSVP.objects.all()
    return render(request, 'rsvp/list.html', { "rsvps": rsvps })

def rsvp_delete(request, pk=None):
    instance = get_object_or_404(RSVP, pk=pk)
    instance.delete()
    return redirect("rsvp:list")

class RSVPCreate(CreateView):
    model = RSVP
    fields = ['name','numGuests']
    template_name = 'rsvp/add.html'
    success_url = '/rsvp'