from django.forms import TimeField
from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Reservation, Menu, Table
from django.contrib.auth.models import User
from datetime import datetime, time, timedelta   
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse



class Home ( View ) :
    def get(self,request ):
        context = { 'fixed_header': True }
        return render(request , 'myapp/index.html' , context )
    



class MyReservations (LoginRequiredMixin , View ):
    login_url = '/accounts/login'

    def get( self, request ):

        # get the current user logged in using the session. 
        # query reservations using the logged in user id.
        reserved = Reservation.objects.filter(user=request.user )
        print( reserved )
        context = { 'reservations' : reserved }
        return render( request , 'myapp/reservations.html' , context )
    # def delete 
    def delete(self, request, pk=None):
        print('hit api route...')
        reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
        reservation.delete()
        return JsonResponse({'success': True})

# HTTP when you communicate between client and server you
# do so using either a GET, POST, PUT, , PATCH , DELETE .. 

def generate_time_options(start_time, end_time, interval_minutes):
    times = []
    current_time = start_time
    while current_time < end_time:
        
        times.append(current_time.strftime("%H:%M"))
        current_time = (datetime.combine(datetime.min, current_time) + timedelta(minutes=interval_minutes)).time()
    return times



class ReservedView(View):
    def get(self, request, reservation_id):
        """
        Fetches and displays reservation details after successful booking.
        """
        try:
            start_time = time(13, 0)  # 1:00 PM
            end_time = time(19, 0)    # 7:00 PM
            interval_minutes = 30

            time_options = generate_time_options(start_time, end_time, interval_minutes)
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return render(request, 'myapp/reserved.html', {'error': "Reservation not found."})

        return render(request, 'myapp/reserved.html', 
                      {'reservation': reservation ,  
                       'time_options': time_options
                    })

    def put(self, request ):
        return JsonResponse({
            'success': True 
        })

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
            user=request.user,
            date=date,
            time=time_object,
            table=table,
            party_size=party_size,
            children=children,
            dietary_notes=dietary_notes
        )

        return render(request, 'myapp/reserved.html', {'reservation': reservation})


class MenuPage ( View ) :
    def get(self,request ):
        # fetch data from the db and then load that into the html render.

        menu_breakfast = Menu.objects.filter(type='breakfast')
        menu_lunch  = Menu.objects.filter(type='lunch')
        menu_dinner = Menu.objects.filter(type='dinner')


        # pass the array to the template / view
        context = {
            'breakfast': menu_breakfast,
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

        print( username , password )

        # we would want to check that a username or email does not already exist in the user db..
        if User.objects.filter( username=username ).exists():
            messages.error( request, 'Username already exists')
            return redirect('register')
        user = User.objects.create_user( username=username, password=password, email=email )
        user.save()
        messages.success( request , 'Registration was successful')
        return redirect('register')
    else:
        return render( request , 'registration/register.html')