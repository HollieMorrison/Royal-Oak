from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import BookingForm
from .models import Booking

# CreateView handles displaying and processing the booking form for new bookings
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_form.html"
    success_url = reverse_lazy("my_bookings")  # Redirect after successful booking

    def form_valid(self, form):
        # Automatically assign the booking to the logged-in user
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        messages.success(self.request, "Booking created!")
        return resp


# ListView displays a list of bookings. A user sees their own, staff see all.
class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            # Staff can see all bookings
            return qs.order_by("-created_at")
        # Normal users only see their own bookings
        return qs.filter(user=self.request.user).order_by("-created_at")


# Mixin to ensure users can only modify their own bookings (unless staff)
class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_staff or obj.user == self.request.user


# UpdateView lets users edit an existing booking
class BookingUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_form.html"
    success_url = reverse_lazy("my_bookings")

    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, "Booking updated!")
        return resp


# DeleteView handles cancellations (deleting a booking)
class BookingDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking_confirm_delete.html"
    success_url = reverse_lazy("my_bookings")

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Booking cancelled.")
        return super().delete(*args, **kwargs)
