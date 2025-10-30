from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

# This represents a physical table in the restaurant
class Table(models.Model):
    name = models.CharField(max_length=20, unique=True)  # Table name
    seats = models.PositiveIntegerField()  # Number of seats available

    def __str__(self):
        # This is a display name and seat in admin or template
        return f"{self.name} ({self.seats})"


# This stores individual booking records made by users
class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # Links booking to the user who made it
    date = models.DateField()  # Date of reservation
    time = models.TimeField()  # Time of reservation
    party_size = models.PositiveIntegerField()  # Number of guests
    table = models.ForeignKey(Table, on_delete=models.PROTECT)  # Which table is booked
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for record creation

    def clean(self):
       
        # Prevent booking for past dates
        if self.date < date.today():
            raise ValidationError("You can’t book for a past date.")

        # Prevent multiple bookings for the same table, date, and time
        clash = Booking.objects.filter(
            date=self.date, time=self.time, table=self.table
        ).exclude(id=self.id).exists()
        if clash:
            raise ValidationError("That table is already booked for that slot.")

        # Prevent party sizes larger than the table capacity
        if self.party_size > self.table.seats:
            raise ValidationError("Party size exceeds table capacity.")

    def __str__(self):
        # This is for admin and debugging
        return f"{self.user} — {self.date} {self.time} — {self.table}"
