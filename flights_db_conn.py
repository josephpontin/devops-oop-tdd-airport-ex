from pyodbc_connection import *

class FlightDBConnection(MSSQLConnection):

    def list_all_flights(self):
        query = f"SELECT * FROM Flights ORDER BY flight_number"
        # print(query)
        data = self.sql_query(query)
        str_to_output = ''
        while True:
            record = data.fetchone()
            if record is None:
                break
            str_to_output += f"Flight No: {record.flight_number}, Origin: {record.origin}, " \
                             f"Destination: {record.destination}\n"
        return str_to_output

    def create_flight(self):
        flight_number = input('Enter the number of the flight')
        origin = input('Enter the origin of the flight')
        destination = input('Enter the destination of the flight')
        plane_id = input('Enter the id of the plane')
        query = f"INSERT INTO Flights (flight_number, origin, destination, plane_id) VALUES" \
                f"('{flight_number}', '{origin}', '{destination}', '{plane_id}')"
        # print(query)
        self.sql_query(query)
        self.docker_flights.commit()
        return 'Flight added'

    def find_flight(self, flight_no):
        query = f"SELECT * FROM Flights WHERE flight_number = '{flight_no}'"
        data = self.sql_query(query)
        record = data.fetchone()
        return record.ID

    def get_pax(self):
        flight_no = input('Enter the number of the flight you wish to view passengers for...')
        query = f"SELECT first_name, last_name, passport_no FROM Flights " \
                f"JOIN PassengersOnFlights ON Flights.ID = PassengersOnFlights.flight_id " \
                f"JOIN Passengers ON PassengersOnFlights.passenger_id = Passengers.ID " \
                f"WHERE Flights.flight_number = '{flight_no}'"
        data = self.sql_query(query)
        str_to_output = ''
        while True:
            record = data.fetchone()
            if record is None:
                break
            str_to_output += f"Name: {record.first_name} {record.last_name}, " \
                             f"Passport Number: {record.passport_no}\n"
        return str_to_output

    def print_pax(self):
        flight_no = input('Enter the number of the flight you wish to print passengers for...')
        query = f"SELECT first_name, last_name, passport_no FROM Flights " \
                f"JOIN PassengersOnFlights ON Flights.ID = PassengersOnFlights.flight_id " \
                f"JOIN Passengers ON PassengersOnFlights.passenger_id = Passengers.ID " \
                f"WHERE Flights.flight_number = '{flight_no}'"
        data = self.sql_query(query)
        with open(f"{flight_no}.txt", 'w') as open_file:
            while True:
                record = data.fetchone()
                if record is None:
                    break
                str_to_output = f"Name: {record.first_name} {record.last_name}, " \
                                 f"Passport Number: {record.passport_no}\n"
                open_file.write(str_to_output)
        return f'Passenger list written to file {flight_no}.txt'