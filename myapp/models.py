from datetime import date

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=20, unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.seats})"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # No bookings in the past
        if self.date < date.today():
            raise ValidationError("You can’t book for a past date.")

        # No double bookings on same table/date/time
        clash = (
            Booking.objects.filter(date=self.date, time=self.time, table=self.table)
            .exclude(id=self.id)
            .exists()
        )
        if clash:
            raise ValidationError("That table is already booked for that slot.")

        # Party must fit the table
        if self.party_size > self.table.seats:
            raise ValidationError("Party size exceeds table capacity.")

    def __str__(self):
        return f"{self.user} — {self.date} {self.time} — {self.table}"
