class Plane:

    list_of_planes = []

    def __init__(self, number):
        self.number = number
        Plane.list_of_planes.append(self)
