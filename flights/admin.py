from django.contrib import admin
from .models import Flight, Booking

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'destination', 'date', 'time', 'price_range')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('flight', 'seat_number', 'passenger_name')
