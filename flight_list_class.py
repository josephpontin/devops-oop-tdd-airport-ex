class Flight():

    def __init__(self, plane_no = None, destination = None, origin = None, pass_list = None):
        if pass_list is None:
            self.pass_list = []
        else:
            self.pass_list = pass_list
        self.plane = plane_no
        self.destination = destination
        self.origin = origin

    def add_plane(self, number):
        self.plane = number

    def add_dest(self, dest):
        self.destination = dest

    def add_origin(self, origin):
        self.origin = origin

    def add_passenger(self, passenger):
        self.pass_list.append(passenger)