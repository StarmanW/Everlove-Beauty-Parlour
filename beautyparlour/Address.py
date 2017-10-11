'''
Address class

Created by StarmanW - 25 August 2017
'''

class Address(object):
    # Parameterised constructor
    def __init__(self, street, zip, city, state):
        self.__street = street
        self.__zip = zip
        self.__city = city
        self.__state = state

    # Get full address function
    def get_full_address(self):
        return '{}, {}, {}, {}'.format(self.__street, self.__zip, self.__city, self.__state)