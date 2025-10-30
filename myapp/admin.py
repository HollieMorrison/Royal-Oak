from django.contrib import admin
from .models import Table, Booking

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("name", "seats")
    search_fields = ("name",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "time", "table", "party_size", "created_at")
    list_filter = ("date", "time", "table")
    search_fields = ("user__username", "table__name")
