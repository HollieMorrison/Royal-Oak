from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50, unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.seats} seats)"


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return (
            f"{self.user.username} - {self.date} {self.time} - "
            f"{self.table.name}"
        )

    def clean(self):
        errors = {}

        if self.date and self.date < date.today():
            errors["date"] = "Bookings cannot be made in the past."

        if self.party_size and self.table:
            if self.party_size > self.table.seats:
                errors["party_size"] = (
                    "Party size cannot exceed table capacity."
                )

        if self.table and self.date and self.time:
            existing_booking = Booking.objects.filter(
                table=self.table,
                date=self.date,
                time=self.time,
            )
            if self.pk:
                existing_booking = existing_booking.exclude(pk=self.pk)

            if existing_booking.exists():
                errors["table"] = (
                    "This table is already booked for that date and time."
                )

        if errors:
            raise ValidationError(errors)
