from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

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
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = RoyalOakUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking created successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm()

    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user).order_by(
        "date", "time")
    return render(request, "bookings/list.html", {"bookings": bookings})


@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            updated_booking.user = request.user
            updated_booking.save()
            messages.success(request, "Booking updated successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking)

    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect("my_bookings")

    return render(request,
                  "bookings/booking_confirm_delete.html",
                  {"booking": booking})


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def staff_dashboard(request):
    bookings = Booking.objects.all().order_by("date", "time")
    return render(request, "staff/dashboard.html", {"bookings": bookings})


@login_required
def account(request):
    return render(request, "account.html")
