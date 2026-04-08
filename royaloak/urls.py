from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("reserve/", views.booking_create, name="reserve"),
    path("my-bookings/", views.my_bookings, name="my_bookings"),
    path(
        "booking/<int:pk>/edit/",
        views.booking_edit,
        name="booking_edit",
    ),
    path(
        "booking/<int:pk>/delete/",
        views.booking_delete,
        name="booking_delete",
    ),
    path(
        "staff/dashboard/",
        views.staff_dashboard,
        name="staff_dashboard",
    ),
    path("account/", views.account, name="account"),
]
