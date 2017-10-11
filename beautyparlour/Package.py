'''
Package class

Created by StarmanW - 25 August 2017
'''

#Import
import re, utility


class Package(object):
    #Parameterised constructor
    def __init__(self, package_id, package_name, package_price, treatment1, treatment2):
        self.__package_id = package_id
        self.__package_name = package_name
        self.__package_price = package_price
        self.__treatment1 = treatment1
        self.__treatment2 = treatment2

    # Getters
    @property
    def package_id(self):
        return self.__package_id

    @property
    def package_name(self):
        return self.__package_name

    @property
    def package_price(self):
        return self.__package_price

    @property
    def treatment1(self):
        return self.__treatment1

    @property
    def treatment2(self):
        return self.__treatment2

    # Setters
    @package_id.setter
    def package_id(self, package_id):
        self.__package_id = package_id

    @package_name.setter
    def package_name(self, package_name):
        self.__package_name = package_name

    @package_price.setter
    def package_price(self, package_price):
        self.__package_price = package_price

    @treatment1.setter
    def treatment1(self, treatment1):
        self.__treatment1 = treatment1

    @treatment2.setter
    def treatment2(self, treatment2):
        self.__treatment2 = treatment2

    @classmethod
    # Register a new package
    def register_package(cls, package_list, treatment_list):
        # Local variables declaration
        new_pack, treat1_index, treat2_index = 0, 0, 0

        # Get user inputs
        while True:
            try:
                num_of_packg = int(input('Enter the amount of package to add (0 for return to menu): '))
                break
            except ValueError:
                print('Invalid input data type, please input only number.\n')

        if num_of_packg == 0: return

        # Loop to repeat the process if registering multiple package
        for i in range(0, int(num_of_packg)):
            treat1_found = treat2_found = False
            print('\nPackage No. ' + str(i + 1))
            print('-' * 18)

            packg_name = input('Enter new package name       : ')
            packg_price = input('Enter new package price      : RM ')

            while not (re.match('^\d{2,}(\.\d{2})?$', packg_price)):
                print('Invalid input data type, please input only number. (RM 50.00)\n')
                packg_price = input('Enter new package price      : RM ')

            # Prompt user whether to display the treatments list or not
            display_treat_menu = input('Display treatments list? (Y/N) : ')

            while not (re.match('^[YyNn]$', display_treat_menu)):
                print('Invalid input, please try again with Y or N only.\n')
                display_treat_menu = input('Display treatments list? (Y/N) : ')

            # Display the menu if input is 'Y'
            if re.match('^[Yy]$', display_treat_menu):
                utility.display_treatment(treatment_list)

            # Prompt for the first treatment
            while not treat1_found:
                treat1 = input('Enter treatment 1 ID : ')

                while not re.match('^\w{2}\d{3}$', treat1):
                    print('Invalid treatment ID, please try again with proper ID (e.g. HC001).\n')
                    treat1 = input('Enter treatment 1 ID : ')

                for i in range(0, len(treatment_list)):
                    if treatment_list[i].treatment_code == treat1:
                        treat1_index = i
                        treat1_found = True
                        break
                    else:
                        treat1_found = False

                if not treat1_found:
                    print('Treatment not found in the system, please ensure the entered treat ID exists.\n')

            # Prompt for the second treatment
            while not treat2_found:
                treat2 = input('Enter treatment 2 ID : ')

                while not re.match('^\w{2}\d{3}$', treat2):
                    print('Invalid treatment ID, please try again with proper ID (e.g. HC001).\n')
                    treat2 = input('Enter treatment 1 ID : ')

                for i in range(0, len(treatment_list)):
                    if treatment_list[i].treatment_code == treat2:
                        treat2_index = i
                        treat2_found = True
                        break
                    else:
                        treat2_found = False

                if not treat2_found:
                    print('Treatment not found in the system, please ensure the entered treat ID exists.\n')

            package_list.append(
                Package(('PK%03d' % (len(package_list) + 1)), packg_name, float(packg_price), treatment_list[treat1_index],
                        treatment_list[treat2_index]))
            new_pack += 1
            existed_packg = package_list[len(package_list) - 1].__eq__(package_list)

            if existed_packg:
                del package_list[len(package_list) - 1]
                print('\nCannot be added into the system. Same package already existed in the system.')
                new_pack -= 1

        print('No new package added into the system.\n') if new_pack == 0 else print('\n' + str(new_pack) + ' new package(s) successfully added into the system.')

    # Overriding __str__ function
    def __str__(self):
        return '%-10s \t\t %-25s \t %-60s \t %-60s \t\t\t RM %8.2f' % (self.__package_id, self.__package_name, self.__treatment1.treatment_desc, self.__treatment2.treatment_desc, self.__package_price)

    # Overloading __eq__ function
    def __eq__(self, package_list):
        same_package = False

        # Check for same package
        for x in range(0, len(package_list) - 1):
            if(self.__package_name == package_list[x].package_name and self.__package_price == package_list[x].package_price):
                same_package = True

        # Return true if it is the same package
        return same_package