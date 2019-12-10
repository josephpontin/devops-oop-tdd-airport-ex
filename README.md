# Airport Manager

This program is an example of using TDD and OOP. This involved creating classes and methods as well as using pytest to ensure the program works as intended.

This program consists of 4 files:
- flight_list_class
    - This contains the class to create a flight instance with details of origin, destination, passenger list and plane number
- plane_class
    - This contains the class to create a  plane instance, using only the plane number.
- passenger_class
    - This contains the class to create a passenger, taking name and passport number
- airport_test
    - This is ran using pytest to test the other files are working properly.
    - This was the first file made as part of TDD

#### Definition of done

- Documentation Complete
- In its own project repository on GitHub
- Test file passes (see below for tests)

#### Tests to pass
###### Passengers
- As a user I can 
    - Create a passenger using name and passport number.
    - Create 'Joana Thomson' with passport number B343123
    - Create 'Birt Kuman' with passport B13927
    - Get an error if I try to create a user without name and/or passport number.
    
###### Plane
- As a user I can
    - Create a plane with the plane number.
    
###### Flight
- As a user I can 
    - Create a flight without any specific information.
    - Add a plane to a flight
    - Add a destination to a flight
    - Add an origin to a flight
    - Add a passenger to the passenger list
    - Have the passenger list as a list of objects
    - Remove a passenger from the passenger list
