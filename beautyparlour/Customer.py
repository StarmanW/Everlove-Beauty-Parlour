'''
Customer class. This class inherits from the superclass "Person.py"

Created by StarmanW - 25 August 2017
'''

# Imports
import re, datetime
from Person import Person


class Customer(Person):
    # Parameterised constructor
    def __init__(self, member_id, fname, lname, date_member_since, contact_number, street, zip, city, state):
        Person.__init__(self, fname, lname, street, zip, city, state, contact_number)
        self.member_id = member_id
        self.date_member_since = date_member_since

    # Getters
    @property
    def member_id(self):
        return self.__member_id

    @property
    def date_member_since(self):
        return self.__date_member_since

    # Setters
    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id

    @date_member_since.setter
    def date_member_since(self, date_member_since):
        self.__date_member_since = date_member_since

    # Registration for customer
    @classmethod
    def register_customer(cls, customer_list):
        # Local variable declaration
        new_cust = 0

        while True:
            try:
                num_of_new_cust = int(input('Enter the amount of customer to register (0 for return to menu): '))
                break
            except ValueError:
                print('Invalid input, please enter only numbers.\n')

        if num_of_new_cust == 0:
            return

        for i in range(0, int(num_of_new_cust)):
            print('\nCustomer No. ' + str(i + 1))
            print('-' * 18)

            # Prompt for first name
            fname = input('Enter customer first name: ')

            while not re.match('^[A-Za-z\- ]{3,}$', fname):
                print('Invalid input data type, please input only alphabetic.\n')
                fname = input('Enter customer first name: ')

            # Prompt for last name
            lname = input('Enter customer last name : ')

            while not re.match('^[A-Za-z\- ]{3,}$', lname):
                print('Invalid input data type, please input only alphabetic.\n')
                lname = input('Enter customer last name: ')

            # Customer's street address
            street = input('Enter street address     : ')

            # Customer's zip address
            zip = input('Enter zip                : ')

            while not re.match('^[0-9]{5}$', zip):
                print('Invalid input, please input only numbers and ensure it is a 5 digit zip code.\n')
                zip = input('Enter zip                : ')

            # Customer's city address
            city = input('Enter city               : ')

            while not re.match('^[A-Za-z\- ]{3,}$', city):
                print('Invalid input data type, please enter only alphabetic.\n')
                city = input('Enter city               : ')

            # Cusotmer's state address
            state = input('Enter state              : ')

            while not re.match('^[A-Za-z\- ]{3,}$', state):
                print('Invalid input data type, please enter only alphabetic.\n')
                state = input('Enter state              : ')

            # Customer's contact number
            contact_num = input('Enter contact nummber    : ')

            while not re.match('^\d{3}\\-\d{7,8}$', contact_num):
                print(
                    'Invalid format or data type, please ensure to input the correct format and data type. e.g. 016-8887469\n')
                contact_num = input('Enter contact nummber    : ')

            customer_list.append(
                Customer(('CUST%04d' % (len(customer_list) + 1)), fname, lname,
                         datetime.date.today().strftime('%d-%b-%Y'), contact_num, street,
                         int(zip), city, state))
            new_cust += 1

            # Remove the latest customer in the list if its an existing customer
            if customer_list[(len(customer_list) - 1)].__eq__(customer_list):
                del customer_list[(len(customer_list) - 1)]
                print('\nCannot be added into the system. Same customer already existed in the system.')
                new_cust -= 1

        # Check the counter to display appropriate message
        print('No new customer member added into the system.\n') if new_cust == 0 else \
            print('\n' + str(new_cust) + ' new customer(s) has been successfully added into the system.\n')

    # Overriding __str__ method
    def __str__(self):
        return '%-12s \t %s \t %-10s' % (self.member_id, super().__str__(), self.__date_member_since)

    # Equals method to check the same customer existed or not
    def __eq__(self, customer_list):
        same_customer = False

        # Check for same customer name
        for x in range(0, len(customer_list) - 1):
            if (self._name.get_full_name() == customer_list[
                x]._name.get_full_name() and self._address.get_full_address() ==
                customer_list[x]._address.get_full_address() and self._contact_number() == customer_list[
                x]._contact_number):
                same_customer = True

        # Return true if it is the same customer
        return same_customer
