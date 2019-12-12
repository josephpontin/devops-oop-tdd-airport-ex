import pyodbc

class MSSQLConnection:

    def __init__(self):

        # These are our variables to connect
        server = 'localhost,1433'
        database = 'Flights'
        username = 'SA'
        password = 'Passw0rd2018'

        # This makes the connection
        self.docker_flights = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

        # This makes the cursor
        self.cursor = self.docker_flights.cursor()

    def sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

#row = cursor.fetchall()

#print(row)