from django.urls import path , include
from . import views  

urlpatterns = [
    path('' , views.Home.as_view() , name='home' ),
    path('restaurant/menu' , views.MenuPage.as_view() , name='menu' ),
    path('about' , views.About.as_view() , name='about'),
    path('reservations', views.Reservations.as_view(), name="reservations" ),
    path('accounts/' , include('django.contrib.auth.urls') ),
    path('reserved/<int:reservation_id>/', views.ReservedView.as_view(), name='reserved'),
    path('register' , views.register , name="register" )
]