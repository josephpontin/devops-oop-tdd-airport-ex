from pyodbc_connection import *
from flights_db_conn import *
from passenger_db_conn import *


class FlightPassListDBConnection(MSSQLConnection):

    def add_pass_to_flight(self):
        flight_number = input('Enter the number of the flight')
        flight_id = FlightDBConnection().find_flight(flight_number)
        choice = input('Would you like to view available passengers before choosing the passenger ID? y/n')
        if choice.lower() == 'y':
            print(PassengerDBConnection().list_all_passengers())
        passenger_id = input('Enter the ID of the passenger to add')
        query = f"INSERT INTO PassengersOnFlights (passenger_id, flight_id) VALUES" \
                f"('{passenger_id}', '{flight_id}')"
        # print(query)
        self.sql_query(query)
        self.docker_flights.commit()
        return 'Flight added'
