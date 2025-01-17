from django.urls import path
from . import views  
from django.contrib.auth import views as default_auth_views

urlpatterns = [
    path('' , views.Home.as_view() , name='home' ),
    path('restaurant/menu' , views.Menu.as_view() , name='menu' ),
    path('about' , views.About.as_view() , name='about'),
    path('reservations', views.Reservations.as_view(), name="reservations" ),
    path('register' , views.register , name="register" ),
    path('loginview' , views.login_view , name="loginview")
]