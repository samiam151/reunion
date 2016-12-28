from django.contrib import admin

from .models import Event

# Register your models here.
class EventAdminModel(admin.ModelAdmin):
    '''Admin Model for the Events App'''
    list_display = ['name', 'description', 'time_start', 'time_end', 'location']
    list_display_links = ["name"]
    list_editable = ['description', 'location']

    class Meta:
        model = Event

admin.site.register(Event, EventAdminModel)