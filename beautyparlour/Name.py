'''
Name class

Created by StarmanW - 25 August 2017
'''

class Name(object):
    # Parameterised constructor
    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    # Get full name function
    def get_full_name(self):
        return '{} {}'.format(self.__fname, self.__lname)
