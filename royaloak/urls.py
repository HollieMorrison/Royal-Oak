from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),

    path("reserve/", views.BookingCreateView.as_view(), name="reserve"),
    path("my-bookings/", views.MyBookingsView.as_view(), name="my_bookings"),
    path("booking/<int:pk>/edit/", views.BookingUpdateView.as_view(), name="booking_edit"),
    path("booking/<int:pk>/delete/", views.BookingDeleteView.as_view(), name="booking_delete"),

    path("staff/dashboard/", views.staff_dashboard, name="staff_dashboard"),
]
