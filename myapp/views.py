from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BookingForm, RoyalOakUserCreationForm
from .models import Booking


def home(request):
    return render(request, "home.html")


def menu(request):
    return render(request, "menu.html")


def signup(request):
    if request.method == "POST":
        form = RoyalOakUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RoyalOakUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/list.html"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("my_bookings")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Booking created successfully.")
        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("my_bookings")

    def test_func(self):
        return self.get_object().user == self.request.user


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = "bookings/booking_confirm_delete.html"
    success_url = reverse_lazy("my_bookings")

    def test_func(self):
        return self.get_object().user == self.request.user


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def staff_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, "staff/dashboard.html", {"bookings": bookings})
