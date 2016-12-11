from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
def rsvp_list(request):
    return render(request, 'rsvp/list.html')