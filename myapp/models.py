from django.db import models
from django.utils.translation import gettext_lazy as _

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)  # Unique identifier for each table
    capacity = models.PositiveIntegerField()  # Maximum number of guests the table can accommodate
    location = models.CharField(max_length=100, blank=True)  # Optional, e.g., "Window", "Patio"

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        PENDING = 'Pending', _('Pending')
        CONFIRMED = 'Confirmed', _('Confirmed')
        CANCELLED = 'Cancelled', _('Cancelled')

    name = models.CharField(max_length=100)  # Name of the person booking
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # Link to the Table model
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    
    children = models.PositiveIntegerField(default=0)
    dietary_notes = models.TextField(blank=True)  # More descriptive dietary field
    status = models.CharField(
        max_length=10, 
        choices=ReservationStatus.choices, 
        default=ReservationStatus.PENDING
    )

    def clean(self):
        # Ensure party size does not exceed table capacity
        if self.party_size > self.table.capacity:
            raise ValueError("Party size cannot exceed the table capacity.")

    def __str__(self):
        return (
            f"Reservation for {self.name} on {self.date} at {self.time}, "
            f"Party Size: {self.party_size} (Children: {self.children}), "
            f"Table {self.table.table_number}, Status: {self.status}"
        )


class MealType(models.TextChoices):
    BREAKFAST = 'breakfast', _('Breakfast')
    LUNCH = 'lunch', _('Lunch')
    DINNER = 'dinner', _('Dinner')


class Menu(models.Model):
    name = models.CharField(max_length=100)  # Name of the menu item
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Currency support
    type = models.CharField(choices=MealType.choices, default=MealType.LUNCH, max_length=30)

    def __str__(self):
        return f"{self.name} - £{self.price} ({self.type})"
