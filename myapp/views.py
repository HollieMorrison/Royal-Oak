from django.forms import TimeField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Reservation, Menu, Table
from django.contrib.auth.models import User
from datetime import date, time, datetime, timedelta
from django.contrib import messages

# Create your views here.

class Home ( View ) :
    def get(self,request ):
        return render(request , 'myapp/index.html')

# HTTP when you communicate between client and server you
# do so usi g either a GET, POST, PUT, DELETE .. 

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

def generate_time_options(start_time, end_time, interval_minutes):
    times = []
    current_time = start_time
    while current_time < end_time:
        # Format the time as a string compatible with TimeField (HH:MM)
        times.append(current_time.strftime("%H:%M"))
        current_time = (datetime.combine(datetime.min, current_time) + timedelta(minutes=interval_minutes)).time()
    return times


class Reservations ( View ) :
    def get ( self , request ): 

        # time_options = generate_time_options(time(17, 0), time(21, 0), 15)  # 5 PM to 9 PM with 15 min intervals
        # Example usage
        start_time = time(17, 0)  # 5:00 PM
        end_time = time(21, 0)    # 9:00 PM
        interval_minutes = 15

        time_options = generate_time_options(start_time, end_time, interval_minutes)
        return render( request , 'myapp/reserve.html', {'time_options': time_options} )
    
    def post(self, request):
        # Handle the form submission
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        party_size = request.POST.get('party_size')
        children = request.POST.get('children')
        dietaryNotes = request.POST.get('dietary')

        time_object = datetime.strptime(time, "%H:%M").time()

        # Assign to a TimeField
        time_field = TimeField()
        time_value = time_field.to_python(time_object)

        print( time_field )

        # # find a available table
        table = Table.objects.get(id=1)

        # Save the reservation to the database
        Reservation.objects.create(
            name=name,
            date=date,
            time=time,
            table=table,
            party_size=party_size,
            children=children,
            dietary_notes=dietaryNotes
        )
        
        # Redirect back to the same page to display updated reservations
        return redirect('reservations')

class Menu ( View ) :
    def get(self,request ):
        # fetch data from the db and then load that into the html render.

        menu_lunch = Menu.objects.filter(type='lunch')
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
    
# views that just return data.
def login_view ( request ):
    if  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print( username, password )
        return redirect('loginview')
    else:
        return render( request , 'myapp/auth/login.html' )
    
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