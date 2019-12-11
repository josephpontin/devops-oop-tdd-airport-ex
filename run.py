from functions import *
passengers = []


while True:
    print('Press 1 to add a passenger')
    print('Press 2 to list all flights')
    print('Press 3 to add a passenger to a flight')
    print('Press 4 to create a flight')
    user_input = input('....')
    interpret_input(user_input, passengers)