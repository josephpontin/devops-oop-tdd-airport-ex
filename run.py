from flightpasslistdb import *

passengers = []


passengers_table = PassengerDBConnection()
flights_table = FlightDBConnection()
flight_pass_list_db = FlightPassListDBConnection()

while True:
    print('Press 1 to add a passenger')
    print('Press 2 to list all flights')
    print('Press 3 to add a passenger to a flight')
    print('Press 4 to create a flight')
    print('Press 5 for a list of passengers on a flight')
    print('Press 6 for a list of all passengers in the system')
    print('Press 7 to print a list of passengers on a flight to a .txt file')
    user_input = input('....')

    if user_input == '1':
        print(passengers_table.create_passenger())
    elif user_input == '2':
        print(flights_table.list_all_flights())
    elif user_input == '3':
        print(flight_pass_list_db.add_pass_to_flight())
    elif user_input == '4':
        print(flights_table.create_flight())
    elif user_input == '5':
        print(flights_table.get_pax())
    elif user_input == '6':
        print(passengers_table.list_all_passengers())
    elif user_input == '7':
        print(flights_table.print_pax())
    input('Press ENTER to continue')
