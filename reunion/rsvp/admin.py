from django.contrib import admin

# Register your models here.
from .models import RSVP

class RSVPModelAdmin(admin.ModelAdmin):
    '''Admin Model for RSVPs''';
    list_display = ["name", "numGuests", "timestamp", "member", 'id', 'pk']
    list_filter = ["name", "numGuests", "timestamp"]
    
    class Meta:
        model = RSVP

admin.site.register(RSVP, RSVPModelAdmin)
