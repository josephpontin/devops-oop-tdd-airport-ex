from pyodbc_connection import *


class PassengerDBConnection(MSSQLConnection):

    def create_passenger(self):
        first_name = input('Enter the first name of the passenger')
        last_name = input('Enter the last name of the passenger')
        passport_number = input('Enter the passport number of the passenger')
        query = f"INSERT INTO Passengers (first_name, last_name, passport_no) VALUES ('{first_name}', " \
                f"'{last_name}', '{passport_number}')"
        #print(query)
        self.sql_query(query)
        self.docker_flights.commit()
        return 'Passenger added'
