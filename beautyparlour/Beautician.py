'''
Beautician class. This class inherits from the superclass "Person.py"

Created by StarmanW - 25 August 2017
'''

# Imports
import re, datetime
from Person import Person


class Beautician(Person):
    # Parameterised constructor
    def __init__(self, beautician_id, fname, lname, date_joined, specialization, contact_number, street, zip, city,
                 state):
        Person.__init__(self, fname, lname, street, zip, city, state, contact_number)
        self.__beautician_id = beautician_id
        self.__date_joined = date_joined
        self.__specialization = specialization

    # Getters
    @property
    def beautician_id(self):
        return self.__beautician_id

    @property
    def date_joined(self):
        return self.__date_joined

    @property
    def specialization(self):
        return self.__specialization

    # Setters
    @beautician_id.setter
    def beautician_id(self, beautician_id):
        self.__beautician_id = beautician_id

    @date_joined.setter
    def date_joined(self, date_joined):
        self.__date_joined = date_joined

    @specialization.setter
    def specialization(self, specialization):
        self.__specialization = specialization

    # Registration for beautician
    @classmethod
    def register_beautician(cls, beautician_list):
        # Local variable declaration
        new_beau = 0

        while True:
            try:
                num_of_new_beau = int(input('Enter number of beautician to register (0 for return to menu): '))
                break
            except ValueError:
                print('Invalid input, please enter only numbers.\n')

        if num_of_new_beau == 0: return

        for i in range(0, int(num_of_new_beau)):
            print('\nBeautician No. ' + str(i + 1))
            print('-' * 18)

            # Prompt for first name
            fname = input('Enter beautician first name: ')

            while not re.match('^[A-Za-z\- ]{3,}$', fname):
                print('Invalid input data type, please input only alphabetic.\n')
                fname = input('Enter beautician first name: ')

            # Prompt for last name
            lname = input('Enter beautician last name : ')

            while not re.match('^[A-Za-z\- ]{3,}$', lname):
                print('Invalid input data type, please input only alphabetic.\n')
                lname = input('Enter beautician last name: ')

            # Beautician's specialization
            specialization = input('Enter beautician\'s specialization: ')

            while not re.match('^[A-Za-z\- ]{3,}$', specialization):
                print('Invalid input data type, please input only alphabetic.\n')
                specialization = input('Enter beautician\'s specialization: ')

            # Beautician's street address
            street = input('Enter street address     : ')

            # Beautician's zip address
            zip = input('Enter zip                : ')

            while not re.match('^[0-9]{5}$', zip):
                print('Invalid input, please input only numbers and ensure it is a 5 digit zip code.\n')
                zip = input('Enter zip                : ')

            # Beautician's city address
            city = input('Enter city               : ')

            while not re.match('^[A-Za-z\- ]{3,}$', city):
                print('Invalid input data type, please enter only alphabetic.\n')
                city = input('Enter city               : ')

            # Beautician's state address
            state = input('Enter state              : ')

            while not re.match('^[A-Za-z\- ]{3,}$', state):
                print('Invalid input data type, please enter only alphabetic.\n')
                state = input('Enter state              : ')

            # Beautician's contact number
            contact_num = input('Enter contact nummber    : ')

            while not re.match('^\d{3}\\-\d{7,8}$', contact_num):
                print(
                    'Invalid format or data type, please ensure to input the correct format and data type. e.g. 016-8887469\n')
                contact_num = input('Enter contact nummber    : ')

            beautician_list.append(
                Beautician(('BEAU%03d' % (len(beautician_list) + 1)), fname, lname,
                           datetime.date.today().strftime('%d-%b-%Y'), specialization,
                           contact_num, street, int(zip), city, state))
            new_beau += 1
            existed_beau = beautician_list[(len(beautician_list) - 1)].__eq__(
                beautician_list)  # Check if it is an existing beautician

            # Remove the latest beautician in the list if its an existing beautician
            if existed_beau:
                del beautician_list[(len(beautician_list) - 1)]
                print('\nCannot be added into the system. Same beautician already existed in the system.')
                new_beau -= 1

        # Check the counter to display appropriate message
        print('No new beautician member added into the system.\n') if new_beau == 0 else print(
            '\n' + str(new_beau) + ' new beautician(s) has been successfully added into the system.\n')

    # Overriding __str__ method
    def __str__(self):
        return '%-12s \t %-20s \t %-10s \t %-25s \t %-10s \t %-60s' % (
        self.__beautician_id, self._name.get_full_name(), self.__date_joined, self.__specialization,
        self._contact_number, self._address.get_full_address())

    # Equals method to check the same beautician existed or not
    def __eq__(self, beautician_list):
        same_beautician = False

        # Check for same beautician details
        for x in range(0, len(beautician_list) - 1):
            if (self._name.get_full_name() == beautician_list[
                x]._name.get_full_name() and self._address.get_full_address() == beautician_list[
                x]._address.get_full_address() and self._contact_number() == beautician_list[x]._contact_number):
                same_beautician = True

        # Return true if it is the same beautician
        return same_beautician
