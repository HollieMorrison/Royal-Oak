from django.urls import path
from .views import (
    BookingCreateView,
    MyBookingsView,
    BookingUpdateView,
    BookingDeleteView,
)

# Routes for booking functionality
urlpatterns = [
    path("reserve/", BookingCreateView.as_view(), name="reserve"),  # Create booking
    path("bookings/", MyBookingsView.as_view(), name="my_bookings"),  # View list
    path("bookings/<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_edit"),  # Edit
    path("bookings/<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"),  # Delete
]
