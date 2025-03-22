from django.urls import path , include
from . import views  

urlpatterns = [
    path('' , views.Home.as_view() , name='home' ),
    path('restaurant/menu' , views.MenuPage.as_view() , name='menu' ),
    path('about' , views.About.as_view() , name='about'),
    path('reservations', views.Reservations.as_view(), name="reservations" ),
    path('accounts/' , include('django.contrib.auth.urls') ),
    path('myreservations' , views.MyReservations.as_view() , name='myreservations' ),


    path('myreservations/<int:pk>' , views.MyReservations.as_view() , name='myreservation__delete' ),
    path('reserved/<int:reservation_id>/', views.ReservedView.as_view(), name='reserved'),
    path('register' , views.register , name="register" )
]