from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    
    path('select-seat/<int:flight_id>/', views.select_seat, name='select_seat'),

]
