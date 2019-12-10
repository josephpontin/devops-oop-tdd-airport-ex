import pytest
from passenger_class import *
from plane_class import *
from flight_list_class import *


def test_name_number():
    new_passenger_1 = Passenger('Joana Thomson', 'B343123')
    new_passenger_2 = Passenger('Birt Kuman', 'B13927')
    assert new_passenger_1.name == 'Joana Thomson', 'Joanna Thomson was not created'
    assert new_passenger_2.name == 'Birt Kuman', 'Birt Kuman was not created'
    assert new_passenger_1.number == 'B343123', 'Passport number not created'
    assert new_passenger_2.number == 'B13927', 'Passport number not created'


def test_missing_info():
    with pytest.raises(TypeError):
        Passenger()
    with pytest.raises(TypeError):
        Passenger('Joana Thomson')
    with pytest.raises(TypeError):
        Passenger('B343123')


def test_plane_creation():
    test_plane_1 = Plane('2354')
    test_plane_2 = Plane('4269')
    assert test_plane_1.number == '2354', 'Plane not created'
    assert test_plane_2.number == '4269', 'Plane not created'


def test_create_empty_flight():
    empty_flight = Flight()
    assert empty_flight.plane is None, 'Empty flight plane no not none'
    assert empty_flight.destination is None, 'Empty flight has destination'
    assert empty_flight.origin is None, 'Empty flight has origin'
    assert empty_flight.pass_list == [], 'Empty flight does not have empty list of passengers'


def test_add_plane():
    test_plane = Plane('2534')
    test_flight = Flight()
    test_flight.add_plane(test_plane)
    assert test_flight.plane == test_plane, 'Plane num not added successfully'


def test_add_dest():
    test_flight = Flight()
    test_flight.add_destination('Toronto')
    assert test_flight.destination == 'Toronto', 'Destination not added successfully'


def test_add_origin():
    test_flight = Flight()
    test_flight.add_origin('London')
    assert test_flight.origin == 'London', 'Origin not added successfully'


def test_add_passenger():
    new_passenger = Passenger('Joana Thomson', 'B17432')
    test_flight = Flight()
    test_flight.add_passenger(new_passenger)
    assert isinstance(test_flight.pass_list, list), 'Passenger list is not of type list'
    assert isinstance(test_flight.pass_list[0], Passenger), 'Passenger list does not consist of objects'
    assert new_passenger in test_flight.pass_list, 'Passenger not added to flight'

def test_delete_passenger():
    new_passenger_1 = Passenger('Joana Thomson', 'B17432')
    new_passenger_2 = Passenger('Birt Kuman', 'B13927')
    test_flight = Flight()
    test_flight.add_passenger(new_passenger_1)
    test_flight.add_passenger(new_passenger_2)
    test_flight.drop_passenger('Joana Thomson')
    assert new_passenger_1 not in test_flight.pass_list, 'Passenger not removed from flight'
    assert new_passenger_2 in test_flight.pass_list, 'Wrong passenger removed'
