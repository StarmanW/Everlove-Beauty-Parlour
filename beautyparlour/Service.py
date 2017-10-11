'''
Service class

Created by StarmanW - 25 August 2017
'''

# Import
from Treatment import Treatment
import datetime, utility, re


class Service(object):
    # Parameterised constructor
    def __init__(self, service_id, service_date, total_price, customer, beautician, treatment_or_package, is_free_trials):
        self.__service_id = service_id
        self.__service_date = service_date
        self.__total_price = total_price
        self.__customer = customer
        self.__beautician = beautician
        self.__treatment_or_package = treatment_or_package
        self.__is_free_trials = is_free_trials

    # Getters
    @property
    def service_id(self):
        return self.__service_id

    @property
    def service_date(self):
        return self.__service_date

    @property
    def total_price(self):
        return self.__total_price

    @property
    def customer(self):
        return self.__customer

    @property
    def beautician(self):
        return self.__beautician

    @property
    def treatment_or_package(self):
        return self.__treatment_or_package

    @property
    def free_trials(self):
        return "Yes" if self.__is_free_trials else "No"

    # Setters
    @service_id.setter
    def service_id(self, service_id):
        self.__service_id = service_id

    @service_date.setter
    def service_date(self, service_date):
        self.__service_date = service_date

    @total_price.setter
    def total_price(self, total_price):
        self.__total_price = total_price

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @beautician.setter
    def beautician(self, beautician):
        self.__beautician = beautician

    @treatment_or_package.setter
    def treatment_or_package(self, treatment_or_package):
        self.__treatment_or_package = treatment_or_package

    @free_trials.setter
    def free_trials(self, is_free_trials):
        self.__is_free_trials = is_free_trials

    @classmethod
    def new_service(cls, service_list, treatment_list, package_list, customer_list, beautician_list):
        # variables declaration
        referrer_count, serv_choice, discount_rate = 0, 0, 0.0

        # Display the notes before registering any service
        utility.new_service_notes()

        # Check if the dates are holidays or not
        if (datetime.date.today().strftime('%d-%b-%Y') == '28-Jan-2017' or datetime.date.today().strftime('%d-%b-%Y') == '25-JUN-2017' or
            datetime.date.today().strftime('%d-%b-%Y') == '19-OCT-2017' or datetime.date.today().strftime('%d-%b-%Y') == '25-DEC-2017'):
            discount_rate = 0.90

        # Prompt for registration for free trials
        reg_free_trials = input('Register for free-trials? (Y/N): ')

        while not re.match('^([YyNn])$', reg_free_trials):
            print('Invalid input choice, please try again with only \"Y\" or \"N\" as input.\n')
            reg_free_trials = input('Register for free-trials? (Y/N): ')

        # Prompt for the amount of customer to make service
        while True:
            try:
                num_of_serv = int(input('Enter the numbers of service(s) to register: '))
                break
            except ValueError:
                print('Invalid input data type, please input only number.\n')

        # Check how many customer are registering at once and set the refererCount to 1
        # To indicate that one customer brought extra members for registration.
        if num_of_serv == 0: return
        elif (num_of_serv >= 6 or (num_of_serv > 6 and num_of_serv <= 11) or num_of_serv >= 11) and re.match('^([Nn])$', reg_free_trials):
            referrer_count = 1

        # Loop the number of service to register
        for i in range(0, num_of_serv):
            valid_date, treat_found, cust_found, beau_found, pack_found, extra_mem_discount = False, False, False, False, False, 0

            print('\nService No. ' + str(i+1))
            print('-' * 18)

            # while loop to prompt customer ID and find the existing customer member
            while not cust_found:
                # Prompt for the customer ID
                cust_id = input('Enter customer ID (e.g. CUST0001): CUST')
                while not re.match('^\\d{4}$', cust_id):
                    print('Invalid customer ID format, please try again with the proper format.\n')
                    cust_id = input('Enter customer ID (e.g. CUST0001): CUST')

                # Loop throught array to get the object of the entered customer ID
                for a in range(0, len(customer_list)):
                    if customer_list[a].member_id == ('CUST' + cust_id):
                        cust_index = a
                        cust_found = True
                        break
                    else:
                        cust_found = False

                # If customer is not found in the system, display error message
                if not cust_found:
                    print('Customer not found in the system, please try again and ensure the customer member ID is an existing member.\n')

            if re.match('^(N|n)$', reg_free_trials):
                # Prompt for the treatments/packages
                print('\n' + ('~' * 28) + '\n' +
                      '===== List of Services =====\n' +
                      ('~' * 28) + '\n' +
                      "1. Hair care\n" +
                      "2. Skin care\n" +
                      "3. Body care\n" +
                      "4. Bridal service\n" +
                      "5. Package service\n" +
                      ('~' * 28))
                serv_choice = input("Enter the required service care: ")
                while not re.match('^[1-5]{1}$', serv_choice):
                    print("Invalid input choice, please try again with only 1 to 5 as input choice.\n")
                    serv_choice = input('Enter the required service care: ')

                # Display the specific treatments/packages list
                prefix_code = utility.display_specific_treatment(serv_choice, treatment_list, package_list)

                if not (serv_choice == '5'):
                    while not treat_found:
                        # Enter the service/treatments code
                        treat_id = input('Enter service/treatment Code: ')

                        while not re.match('^'+prefix_code+'\\d{3}$', treat_id):
                            print('Invalid treatment code or code format, please try again with the correct format and correct treatment code. (e.g. ' + prefix_code + '001) \n')
                            treat_id = input('Enter service/treatment Code: ')

                        # Loop through array to get the object of the entered treatment code
                        for b in range(0, len(treatment_list)):
                            if treatment_list[b].treatment_code == treat_id:
                                treat_pack_index = b
                                treat_found = True
                                break
                            else:
                                treat_found = False

                        if not treat_found:
                            print("Not an existing treatment/package code, please try again and ensure the correct and existing treatment/package code as input.\n")
                else:
                    while not pack_found:
                        # Enter the package code
                        pack_id = input('Enter package code: PK')

                        while not re.match('^\\d{3}$', pack_id):
                            print('Invalid package code or code format, please try again with the correct format and correct package code. (e.g. PK001) \n')
                            pack_id = input('Enter package code: PK')

                        # Loop through array to get the object of the entered package code
                        for c in range(0, len(package_list)):
                            if package_list[c].get_package_id() == pack_id:
                                treat_pack_index = c
                                pack_found = True
                            else:
                                pack_found = False
            else:
                print('\n' + ('~' * 100) + '\n' +
                      ('=' * 35) + " List of Free Trials Service " + ('=' * 36) + '\n' +
                      ('~' * 100) + '\n')

                utility.display_free_trials(treatment_list)     # Display list of free trials

                while not treat_found:
                    free_treat = input("Enter free-trials treatment ID: ")

                    while not re.match("^(HC|SC|BC)\d{3}$", free_treat):
                        print("Invalid treatment code or code format, please try again with the correct format and correct treatment code. (e.g. HC001) \n")
                        free_treat = input("Enter free-trials treatment ID: ")

                    for d in range(0, len(treatment_list)):
                        if treatment_list[d].treatment_code == free_treat:
                            treat_pack_index = d
                            treat_found = True
                            break
                        else:
                            treat_found = False

                    if not treat_found:
                        print("Invalid free-trials treatment code, please ensure it is the correct free-trials code listed in the table.\n")

            utility.display_beautician_serv(beautician_list)     # Display the list of beautician for the customer to select

            while not beau_found:
                beau_id = input("Enter prefererd beauticians ID: BEAU")

                while not re.match("^\\d{3}$", beau_id):
                    print("Invalid beautician ID format, please try again with the correct format. (e.g. BEAU001)\n")
                    beau_id = input("Enter prefererd beauticians ID: BEAU")

                for e in range(0, len(beautician_list)):
                    if beautician_list[e].beautician_id == ("BEAU" + beau_id):
                        beau_index = e
                        beau_found = True
                        break
                    else:
                        beau_found = False

                if not beau_found:
                    print("Beautician not found in the system, please try again and ensure the beautician ID is an existing beautician.\n")

            while not valid_date:
                serv_date = input("Enter treatment date (e.g. 02-JAN-2017): ")

                while not re.match("^(([0-2][0-9])|([3][0-1]))\\-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\\-\\d{4}$", serv_date):
                    print("Invalid date format, please ensure the correct date format is entered. (e.g. 02-JAN-2017)\n")
                    serv_date = input("Enter treatment date (e.g. 02-JAN-2017): ")

                if re.match("^(Y|y)$", reg_free_trials) and not re.match("^(28-JAN-2017|25-JUN-2017|19-OCT-2017|25-DEC-2017)$", serv_date):
                    print("Invalid date input, free trials only available on specified holidays date. Please try again and ensure the correct date is entered.\n")
                    valid_date = False
                else:
                    valid_date = True

            # Calculation Part
            if re.match("^(N|n)$", reg_free_trials):
                if num_of_serv >= 6 and referrer_count != 0:
                    extra_mem_discount = 0.85
                elif num_of_serv > 6 and num_of_serv <= 11 and (referrer_count != 0):
                    extra_mem_discount = 0.70
                elif num_of_serv >= 11 and referrer_count !=0:
                    extra_mem_discount = 0.50

                referrer_count = 0


                print('\n' + ('~' * 85) + '\n' +
                     ('=' * 35) + " Total payment " + ('=' * 35) + '\n' +
                     ('~' * 85))

                if serv_choice != '5':
                    if discount_rate != 0 and extra_mem_discount != 0:
                        total_price = treatment_list[treat_pack_index].treatment_price * extra_mem_discount * discount_rate
                    elif discount_rate != 0:
                        total_price = treatment_list[treat_pack_index].treatment_price * discount_rate
                    elif extra_mem_discount != 0:
                        total_price = treatment_list[treat_pack_index].treatment_price * extra_mem_discount
                    else:
                        total_price = treatment_list[treat_pack_index].treatment_price
                    print("Selected treatment           : " + treatment_list[treat_pack_index].treatment_code + '-' + treatment_list[treat_pack_index].treatment_desc)
                    print("Treatment price              : RM %7.2f" % treatment_list[treat_pack_index].treatment_price)
                    service_list.append(Service("APT%05d" % (len(service_list) + 1),  serv_date, total_price, customer_list[cust_index], beautician_list[beau_index], treatment_list[treat_pack_index], False))
                else:
                    if discount_rate != 0 and extra_mem_discount != 0:
                        total_price = package_list[treat_pack_index].package_price * extra_mem_discount * discount_rate
                    elif discount_rate != 0:
                        total_price = package_list[treat_pack_index].package_price * discount_rate
                    elif extra_mem_discount != 0:
                        total_price = package_list[treat_pack_index].package_price * extra_mem_discount
                    else:
                        total_price = package_list[treat_pack_index].package_price
                    print("Selected package             : " + package_list[treat_pack_index].package_id + '-' + package_list[treat_pack_index].package_name)
                    print("Package price                : RM %7.2f" % package_list[treat_pack_index].package_price)
                    service_list.append(Service("APT%05d" % (len(service_list) + 1),  serv_date, total_price, customer_list[cust_index], beautician_list[beau_index], package_list[treat_pack_index], False))

                if discount_rate != 0:
                    print("Holidays dicount             : 10%")
                if extra_mem_discount != 0:
                    print("Brought extra member discount: %2.0f%%" % ((1 - extra_mem_discount) * 100))
                print("Total price after discount   : RM %7.2f" % total_price)
                if total_price > 1000:
                    print("Deposit required (50%%)       : RM %7.2f" % (total_price * 0.5))
            else:
                service_list.append(
                    Service("APT%05d" % (len(service_list) + 1), serv_date, 0.0, customer_list[cust_index],
                            beautician_list[beau_index], treatment_list[treat_pack_index], True))


        print('\n' + str(i + 1) + " service(s) has been successfully recorded into the system.\n")

    # Overrride __str__ function
    def __str__(self):
        if type(self.__treatment_or_package) == Treatment:
            return '%s \t\t %-20s \t RM %8.2f \t %-10s \t %-20s \t %-10s \t %-20s \t%-20s \t %-60s \t%-5s' % \
                   (self.__service_id, self.__service_date, self.__total_price, self.__customer.member_id, self.__customer._name.get_full_name(),
                    self.__beautician.beautician_id, self.__beautician._name.get_full_name(), self.__treatment_or_package.treatment_code,
                    self.__treatment_or_package.treatment_desc, self.free_trials)
        else:
            return '%s \t\t %-20s \t RM %8.2f \t %-10s \t %-20s \t %-10s \t %-20s \t%-20s \t %-60s \t%-5s' % \
                    (self.__service_id, self.__service_date, self.__total_price, self.__customer.member_id, self.__customer._name.get_full_name(),
                     self.__beautician.beautician_id, self.__beautician._name.get_full_name(), self.__treatment_or_package.package_id,
                     self.__treatment_or_package.package_name, self.free_trials)

