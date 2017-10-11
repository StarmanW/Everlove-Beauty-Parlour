'''
Person class. Contains composition relationship with Name class and aggregation
relationship with Address class.

Created by StarmanW - 25 August 2017
'''

#Imports
import Name as name, Address as addr

class Person:
    # Parameterised constructor
    def __init__(self, fname, lname, street, zip, city, state, contact_number):
        self._name = name.Name(fname,lname)
        self._address = addr.Address(street,zip,city,state)
        self._contact_number = contact_number

    # toString methods
    def __str__(self):
        return '%-20s \t %-10s \t %-80s' % (self._name.get_full_name(), self._contact_number, self._address.get_full_address())