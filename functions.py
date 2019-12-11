from passenger_class import *
from flight_list_class import *

def interpret_input(user_input, passengers):
    if user_input == '1':
        name = input('Enter passenger name')
        p_num = input('Enter passport number')
        new_passenger = Passenger(name, p_num)
    elif user_input == '2':
        for flight in Flight.list_of_flights:
            print(flight.flight_no, flight.plane,  flight.origin, flight.destination, [i.name for i in flight.pass_list])
    elif user_input == '3':
        name = input('Enter passenger name')
        flight_number = input('Enter flight number')
        for flight in Flight.list_of_flights:
            if flight.flight_no == flight_number:
                for passenger in Passenger.list_of_passengers:
                    if passenger.name == name:
                        flight.add_passenger(passenger)
    elif user_input == '4':
        flight_number = input('Enter plane number')
        plane_number = input('Enter plane number')
        origin = input('Enter origin')
        destination = input('Enter Destination')
        new_flight = Flight(flight_number, plane_number, origin, destination)