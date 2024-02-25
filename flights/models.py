from django.db import models

class Flight(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, default='Unnamed Flight')
    destination = models.CharField(max_length=100, default='Unknown')
    date = models.DateField()
    time = models.TimeField()
    price_range = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return f"{self.name} - {self.number} - {self.destination} - {self.date} {self.time}"

class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)  
    passenger_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Booking for {self.flight.name} - Seat {self.seat_number} - Passenger {self.passenger_name}"
