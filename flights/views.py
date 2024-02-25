from django.shortcuts import get_object_or_404, render, redirect
from .models import Booking, Flight
from django.contrib import messages

def search_flights(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        flights = Flight.objects.filter(destination=destination, date=date)
        return render(request, 'flights/search_results.html', {'flights': flights})
    return render(request, 'flights/search_flights.html')


from django.utils import timezone

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == 'POST':

        selected_seats = request.POST.getlist('seats')
        
        if selected_seats:  
            for seat_number in selected_seats:
                passenger_name = request.POST.get(f'passenger_name_{seat_number}')  # Assuming passenger_name is submitted for each seat
                booking = Booking.objects.create(flight=flight, seat_number=seat_number, passenger_name=passenger_name)
                print(booking)
            
            messages.success(request, f'Flight {flight.name} (#{flight.number}) was successfully booked on {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}.')
            
            print(f'Booking for Flight {flight.name} (#{flight.number}) was successful.')
            
            return redirect('search_flights')
        else:
            messages.error(request, 'Please select at least one seat.')
            return redirect('select_seat', flight_id=flight_id)
    
    return render(request, 'flights/book_flight.html', {'flight': flight})
def select_seat(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    available_seats = range(1, 61)  
    return render(request, 'flights/select_seat.html', {'flight': flight, 'available_seats': available_seats})