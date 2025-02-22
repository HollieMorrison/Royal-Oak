from django.forms import TimeField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Reservation, Menu, Table
from django.contrib.auth.models import User
from datetime import datetime, time, timedelta   
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.

class Home ( View ) :
    def get(self,request ):
        return render(request , 'myapp/index.html')

# HTTP when you communicate between client and server you
# do so usi g either a GET, POST, PUT, DELETE .. 

def generate_time_options(start_time, end_time, interval_minutes):
    times = []
    current_time = start_time
    while current_time < end_time:
        # Format the time as a string compatible with TimeField (HH:MM)
        times.append(current_time.strftime("%H:%M"))
        current_time = (datetime.combine(datetime.min, current_time) + timedelta(minutes=interval_minutes)).time()
    return times

def Reservations_bookings ( request ):
    # retrieve party size and date for booking.
    # retrieve information sent by the client and do something with that.
    # user signing in sends their login username and password.
    # figure out the available times
    date = request.GET.get('date')
    party_size = request.GET.get('party_size')
    # reservations = Reservation.objects.filter(date='2024-12-05').values('time') get reservations for the date selected. 
    # we need the window of opening time ( 1pm - 7pm ) give 30 min window bookings. 
    # then use existing reservations to check that a table that matches party size is available.
    return HttpResponse( date )

class ReservedView(View):
    def get(self, request, reservation_id):
        """
        Fetches and displays reservation details after successful booking.
        """
        try:
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return render(request, 'myapp/reserved.html', {'error': "Reservation not found."})

        return render(request, 'myapp/reserved.html', {'reservation': reservation})


class Reservations (LoginRequiredMixin , View):
    
    login_url = '/accounts/login'

    def get(self, request):
        """
        Handles GET requests by displaying available reservation time slots.
        """
        start_time = time(13, 0)  # 1:00 PM
        end_time = time(19, 0)    # 7:00 PM
        interval_minutes = 30

        time_options = generate_time_options(start_time, end_time, interval_minutes)
        return render(request, 'myapp/reserve.html', {'time_options': time_options})

    def post(self, request):
        """
        Handles POST requests for making reservations.
        Ensures the table is available before saving the reservation.
        """
        name = request.POST.get('name')
        date = request.POST.get('date')
        reservation_time = request.POST.get('time')  # Renamed from `time` to avoid conflicts
        party_size = int(request.POST.get('party_size'))
        children = request.POST.get('children', '0')  # Ensure it's a string
        children = int(children) if children.isdigit() else 0  # Convert safely
        dietary_notes = request.POST.get('dietary', '')

        # Convert string time input to proper time format
        time_object = datetime.strptime(reservation_time, "%H:%M").time()

    
        # Find available tables that can accommodate the party size and are not already booked
        available_tables = Table.objects.filter(capacity__gte=party_size).exclude(
            id__in=Reservation.objects.filter(
                date=date,
                time=time_object
            ).values_list('table_id', flat=True)
        )

        # if party_size less than available tables seat amount by at least 4 seats?

        if not available_tables.exists():
            return render(request, 'myapp/reserve.html', {
                'error': "No available tables for the selected time and party size.",
                'time_options': generate_time_options(time(13, 0), time(19, 0), 30)  # Ensure correct reference to `time`
            })

        # Assign the first available table
        table = available_tables.first()

        # Create and save the reservation
        reservation = Reservation.objects.create(
            name=name,
            date=date,
            time=time_object,
            table=table,
            party_size=party_size,
            children=children,
            dietary_notes=dietary_notes
        )

        return render(request, 'myapp/reserved.html', {'reservation': reservation})


class Menu ( View ) :
    def get(self,request ):
        # fetch data from the db and then load that into the html render.

        menu_lunch  = Menu.objects.filter(type='lunch')
        menu_dinner = Menu.objects.filter(type='dinner')

        print( menu_lunch, menu_dinner )

        # pass the array to the template / view
        context = {
            'lunch': menu_lunch,
            'dinner': menu_dinner
        }
        return render(request , 'myapp/menu.html' , context )
    
class About ( View ) :
    def get (self, request ):
        return render(request , 'myapp/about.html')
    

def register( request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # we would want to check that a username or email does not already exist in the user db..
        if User.objects.filter( username=username ).exists():
            messages.error( request, 'Username already exists')
            return redirect('register')
        user = User.objects.create( username=username, password=password, email=email )
        messages.success( request , 'Registration was successful')
        return redirect('register')
    else:
        return render( request , 'myapp/auth/register.html')