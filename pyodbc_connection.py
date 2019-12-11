import pyodbc

# These are our variables to connect
server = 'localhost,1433'
database = 'Flights'
username = 'SA'
password = 'Passw0rd2018'

# This makes the connection
docker_flights = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# This makes the cursor
cursor = docker_flights.cursor()

cursor.execute("SELECT * FROM Passengers")

row = cursor.fetchall()

print(row)