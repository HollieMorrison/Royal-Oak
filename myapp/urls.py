from django.urls import path
from . import views  

urlpatterns = [
    path('' , views.home.as_view() , name='home' ),
    path('restaurant/menu' , views.menu.as_view() , name='menu' ),
    path('about' , views.about.as_view() , name='about'),
    path('reservations', views.reservations , name="reservations" )
]

