from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public pages
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),

    # Booking pages
    path("reserve/", views.booking_create, name="reserve"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/edit/", views.booking_edit, name="booking_edit"),
    path("bookings/<int:pk>/delete/", views.booking_delete, name="booking_delete"),

    # Staff dashboard
    path("staff/", views.staff_dashboard, name="staff_dashboard"),

    # Account area
    path("account/", views.account, name="account"),

    # Auth: login / logout / signup
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("accounts/signup/", views.signup, name="signup"),
]
