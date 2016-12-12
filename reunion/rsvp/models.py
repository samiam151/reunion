from django.db import models

# Create your models here.
class RSVP(models.Model):
    name = models.CharField(max_length=50)
    numGuests = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{0} => {1}".format(self.name, self.numGuests)