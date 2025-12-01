from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("reserve/", views.booking_create, name="reserve"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/edit/", views.booking_edit, name="booking_edit"),
    path("bookings/<int:pk>/delete/", views.booking_delete, name="booking_delete"),
    path("staff/", views.staff_dashboard, name="staff_dashboard"),
]
