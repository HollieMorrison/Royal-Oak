from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Reservation, Menu
from datetime import datetime, timedelta

# Create your views here.

class Home ( View ) :
    def get(self,request ):
        return render(request , 'myapp/index.html')

# HTTP when you communicate between client and server you
# do so usi g either a GET, POST, PUT, DELETE .. 

def Reservations_bookings ( request ):
    # retrieve information sent by the client and do something with that.
    # user signing in sends their login username and password.
    date = request.GET.get('date')
    reservations = Reservation.objects.filter(date='2024-12-05').values('time')
    print( reservations )
    return HttpResponse( reservations )


class Reservations ( View ) :
    def get ( self , request ): 
        start_time = datetime.strptime("17:00", "%H:%M")  # 5 PM
        end_time = datetime.strptime("21:00", "%H:%M")  # 9 PM
        intervals = []

        while start_time <= end_time:
            intervals.append(start_time.strftime("%H:%M"))  # Format as HH:MM
            start_time += timedelta(minutes=15)  # Increment by 15 minutes

        return render( request , 'myapp/reserve.html', {'intervals': intervals} )
    
    def post(self, request):
        # Handle the form submission
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        party_size = request.POST.get('party_size')
        children = request.POST.get('children')
        dietaryNotes = request.POST.get('dietary')

        # Save the reservation to the database
        Reservation.objects.create(
            name=name,
            date=date,
            time=time,
            party_size=party_size,
            children=children,
            dietaryNotes=dietaryNotes
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

