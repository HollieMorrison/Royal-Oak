from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking


def home(request):
    return render(request, "home.html")


def menu(request):
    return render(request, "menu.html")


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by(
        "-date", "-start_time"
    )
    return render(request, "bookings/list.html", {"bookings": bookings})


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
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking)

    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.delete()
    messages.info(request, "Booking deleted.")
    return redirect("my_bookings")


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def staff_dashboard(request):
    date = request.GET.get("date")
    bookings = Booking.objects.order_by("date", "start_time")

    if date:
        bookings = bookings.filter(date=date)

    return render(request, "staff/dashboard.html", {"bookings": bookings})
