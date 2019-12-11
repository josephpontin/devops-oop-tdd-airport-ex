class Flight:

    list_of_flights = []

    def __init__(self, flight_no = None, plane_no=None, destination=None, origin=None, pass_list=None):
        if pass_list is None:
            self.pass_list = []
        else:
            self.pass_list = pass_list
        self.flight_no = flight_no
        self.plane = plane_no
        self.destination = destination
        self.origin = origin
        Flight.list_of_flights.append(self)

    def add_plane(self, number):
        self.plane = number

    def add_destination(self, dest):
        self.destination = dest

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.pass_list.append(passenger)

    def drop_passenger(self, passenger_name):
        index = 0
        for passenger in self.pass_list:
            if passenger.name == passenger_name:
                break
        self.pass_list.pop(index)
