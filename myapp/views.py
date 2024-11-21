from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class home ( View ) :
    def get(self,request ):
        return render(request , 'myapp/index.html')

def reservations ( request ):
    # retrieve information sent by the client and do something with that.
    # user signing in sends their login username and password.
    return HttpResponse([
            { 'name': 'table 01' , 'party': 4 },
            { 'name': 'table 02' , 'party': 3  }
    ])

class menu ( View ) :
    def get(self,request ):
        # fetch data from the db and then load that into the html render.
        menu_items = [
            { 'name': 'burger and chips' , 'price': '£18' },
            { 'name': 'pizza', 'price': '£14' }
        ]
        # pass the array to the template / view
        context = {
            'food_items': menu_items
        }
        return render(request , 'myapp/menu.html' , context )
    
class about ( View ) :
    def get (self, request ):
        return render(request , 'myapp/about.html')
    
# views that just return data