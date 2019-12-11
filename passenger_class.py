class Passenger:

    list_of_passengers = []

    def __init__(self, name, number):
         self.name = name
         self.number = number
         Passenger.list_of_passengers.append(self)