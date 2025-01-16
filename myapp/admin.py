from django.contrib import admin
from .models import Reservation, Menu, Table

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
  list_display = ('name', 'date', 'time', 'party_size')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'type')


@admin.register(Table)
class TableAdmin( admin.ModelAdmin):
  list_display = ( 'table_number' , 'capacity' , 'location')