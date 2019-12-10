import pytest
from passenger_class import *
from plane_class import *
from flight_list_class import *

def test_name():
    assert Passenger('Joana Thomson', 'B343123').name == 'Joana Thomson', 'Joanna Thomson was not created'
    assert Passenger('Birt Kuman', 'B13927').name == 'Birt Kuman', 'Birt Kuman was not created'

def test_number():
    assert Passenger('Joana Thomson', 'B343123').number == 'B343123', 'Passport number not created'
    assert Passenger('Birt Kuman', 'B13927').number == 'B13927', 'Passport number not created'

def test_missing_info():
    with pytest.raises(TypeError):
        Passenger()

def test_plane_creation():
    assert Plane('2354').number == '2354', 'Plane not created'
    assert Plane('4269').number == '4269', 'Plane not created'

def test_create_empty_flight():
    assert Flight().plane == None, 'Empty flight plane no not none'
    assert Flight().destination == None, 'Empty flight has destination'
    assert Flight().origin == None, 'Empty flight has origin'
    assert Flight().pass_list == [], 'Empty flight does not have empty list of passengers'

def test_add_plane():
    test_plane = Plane('2534')
    test_flight = Flight()
    test_flight.add_plane(test_plane)
    assert test_flight.plane == test_plane, 'Plane num not added successfully'

def test_add_dest():
    test_flight = Flight()
    test_flight.add_dest('Toronto')
    assert test_flight.destination == 'Toronto', 'Destination not added successfully'

def test_add_origin():
    test_flight = Flight()
    test_flight.add_origin('London')
    assert test_flight.origin == 'London', 'Origin not added successfully'

def test_add_passenger():
    new_passenger = Passenger('Joana Thomson', 'B17432')
    test_flight = Flight()
    test_flight.add_passenger(new_passenger)
    assert new_passenger in test_flight.pass_list, 'Passenger not added to flight'
    assert isinstance(test_flight.pass_list, list), 'Passenger list is not of type list'
    assert isinstance(test_flight.pass_list[0], Passenger), 'Passenger list does not consist of objects'