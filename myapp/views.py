from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm
from .models import Booking


def home(request):
    return render(request, "home.html")


@login_required
def my_bookings(request):
    bookings = (
        Booking.objects.filter(user=request.user)
        .order_by("-date", "-start_time")
    )
    return render(request, "bookings/list.html", {"bookings": bookings})


@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.full_clean()
            booking.save()
            messages.success(request, "Booking created!")
            return redirect("my_bookings")
    else:
        form = BookingForm()
    return render(request, "bookings/form.html", {"form": form})


@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.full_clean()
            booking.save()
            messages.success(request, "Booking updated!")
            return redirect("my_bookings")
    else:
        form = BookingForm(instance=booking)
    return render(request, "bookings/form.html", {"form": form})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.delete()
    messages.info(request, "Booking deleted.")
    return redirect("my_bookings")


def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def staff_dashboard(request):
    date = request.GET.get("date")
    qs = Booking.objects.filter(status="CONFIRMED").order_by("date", "start_time")
    if date:
        qs = qs.filter(date=date)
    return render(request, "staff/dashboard.html", {"bookings": qs})
