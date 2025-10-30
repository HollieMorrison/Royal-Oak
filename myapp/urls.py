from django.urls import path

from .views import (
    BookingCreateView,
    BookingDeleteView,
    BookingUpdateView,
    MyBookingsView,
)

urlpatterns = [
    path("reserve/", BookingCreateView.as_view(), name="reserve"),
    path("bookings/", MyBookingsView.as_view(), name="my_bookings"),
    path("bookings/<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_edit"),
    path(
        "bookings/<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"
    ),
]
