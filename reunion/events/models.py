from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    time_start = models.DateTimeField(auto_now = False, auto_now_add=False, blank=False)
    time_end = models.DateTimeField(auto_now = False, auto_now_add=False, blank=False)

    class Meta:
        ordering = ['time_start']
    
    def __str__(self):
        return "{0}: {1}".format(self.name, self.time_start)