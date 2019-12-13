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

    def list_all_passengers(self):
        query = f"SELECT * FROM Passengers ORDER BY ID"
        #print(query)
        data = self.sql_query(query)
        str_to_output = ''
        while True:
            record = data.fetchone()
            if record is None:
                break
            str_to_output += f"ID: {record.ID}, Name: {record.first_name} {record.last_name}, " \
                             f"Passport Number: {record.passport_no}\n"
        return str_to_output