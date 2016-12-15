from django.db import models

# Create your models here.
class RSVP(models.Model):
    MEMBER_CHOICES = (
        ('onesta', 'Onesta'),
        ('cecilia', 'Cecilia'),
        ('priscilla', 'Priscilla'),
        ('lily', 'Lily Mae'),
        ('curly', 'Curly'),
        ('ophelia', 'Ophelia'),
        ('abby', 'Abby'),    
    )

    name = models.CharField(max_length=50)
    numGuests = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    member = models.CharField(max_length=50, choices=MEMBER_CHOICES, unique=False)

    def __str__(self):
        return "{0} => {1}".format(self.name, self.numGuests)
