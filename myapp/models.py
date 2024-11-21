from django.db import models

# Create your models here.

class Reservation( models.Model ):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"{self.name} - { self.date} at {self.time} for {self.party_size}"
    
