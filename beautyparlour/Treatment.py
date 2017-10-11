'''
Treatment class

Created by StarmanW - 25 August 2017
'''

# Import
import re


class Treatment(object):
    # Parameterised constructor
    def __init__(self, treatment_code, treatment_desc, treatment_price, free_trials):
        self.__treatment_code = treatment_code
        self.__treatment_desc = treatment_desc
        self.__treatment_price = treatment_price
        self.__free_trials = free_trials

    # Getters
    @property
    def treatment_code(self):
        return self.__treatment_code

    @property
    def treatment_desc(self):
        return self.__treatment_desc

    @property
    def treatment_price(self):
        return self.__treatment_price

    @property
    def free_trials(self):
        return 'Yes' if self.__free_trials else 'No'

    # Setters
    @treatment_code.setter
    def treatment_code(self, treatment_code):
        self.__treatment_code = treatment_code

    @treatment_desc.setter
    def treatment_desc(self, treatment_desc):
        self.__treatment_desc = treatment_desc

    @treatment_price.setter
    def treatment_price(self, treatment_price):
        self.__treatment_price = treatment_price

    @free_trials.setter
    def free_trials(self, free_trials):
        self.__free_trials = free_trials

    @classmethod
    # Register treatment
    def register_treatment(cls, treatment_list):
        # local variable declaration
        new_treat = 0

        # Prompt for number of treatment to add
        while True:
            try:
                num_of_treat = int(input('Enter the amount of treatment to add (0 for return to menu): '))
                break
            except ValueError:
                print('Invalid input, please enter only numbers.\n')

        if num_of_treat == 0: return

        for i in range(0, int(num_of_treat)):
            print('\nTreatment No. ' + str(i + 1))
            print('-' * 18)

            # Prompt for treatment type
            print(('~' * 36) +
                  '\nChoose the service for the treatment\n' +
                  ('~' * 36) +
                  '\n1. Hair Care\n' +
                  '2. Skin Care\n' +
                  '3. Body Care\n' +
                  '4. Bridal Service\n' +
                  ('~' * 36))
            service_choice = input('Enter service choice: ')

            while not (re.match('^[1-4]$', service_choice)):
                print('Invalid input choice, please try again with only 1 to 4 as option.\n')
                service_choice = input('Enter service choice: ')

            if service_choice == '1':
                treatment_code = 'HC'
                service_name = 'Hair Care'
            elif service_choice == '2':
                treatment_code = 'SC'
                service_name = 'Skin Care'
            elif service_choice == '3':
                treatment_code = 'BC'
                service_name = 'Body Care'
            else:
                treatment_code = 'BS'
                service_name = 'Bridal Service'

            # Prompt for treatment description
            treat_desc = input('Enter new treatment description: ')

            # Prompt for the price
            treat_price = input('Enter new treatment price      : RM ')

            while not (re.match('^\d{2,}(\.\d{2})?$', treat_price)):
                print('Invalid input data type, please input only number. (RM 50.00)\n')
                treat_price = input('Enter new treatment price      : RM ')

            allow_trials = input('Does free trials of this new treatment available during the holidays? (Y/N): ')

            while not (re.match('^[YyNn]$', allow_trials)):
                print('Invalid input, please try again only with \"Y\" or \"N\" as input.\n')
                allow_trials = input('Does free trials of this new treatment available during the holidays? (Y/N): ')

            if re.match('^[Yy]$', allow_trials):
                free_trials = True
            else:
                free_trials = False

            # Add the new treatment
            treatment_list.append(
                Treatment((treatment_code + '%03d' % (len(treatment_list) + 1)), treat_desc, float(treat_price),
                          free_trials))
            new_treat += 1
            existed_treat = treatment_list[(len(treatment_list) - 1)].__eq__(treatment_list)

            if existed_treat:
                del treatment_list[(len(treatment_list) - 1)]
                print('\nCannot be added into the system. Same treatment already existed in the system.')
                new_treat -= 1

        print('No new treatment added into the system.\n') if new_treat == 0 else print(
            '\n' + str(new_treat) + ' new treatment(s) has been successfully added into the system.\n')

    # Override __str__ function
    def __str__(self):
        return '%-15s \t %-60s \t RM %10.2f\t     %-10s' % (
            self.__treatment_code, self.__treatment_desc, self.__treatment_price, self.free_trials)

    # Overload __eq__ function
    def __eq__(self, treatment_list):
        same_treatment = False

        # Check for same treatment name
        for x in range(0, len(treatment_list) - 1):
            if (self.__treatment_desc == treatment_list[x].treatment_desc and self.__treatment_price == treatment_list[
                x].treatment_price and self.free_trials == treatment_list[x].free_trials):
                same_treatment = True

        # Return true if it is the same treatment
        return same_treatment
